#!/usr/bin/env python3
"""
TeX CV 파일을 파싱하여 JSON으로 변환하는 스크립트

이 스크립트는 LaTeX CV 파일들을 읽어서 구조화된 JSON 데이터로 변환합니다.
웹 페이지에서 사용할 수 있는 형태로 데이터를 추출합니다.
"""

import re
import json
import os
from pathlib import Path
from typing import Dict, List, Any
import pandas as pd


class TexCVParser:
    """LaTeX CV 파일을 파싱하는 클래스"""

    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)
        self.cv_data = {
            "personal": {},
            "biography": "",
            "employment": [],
            "education": [],
            "skills": {},
            "projects": [],
            "publications": {
                "early_access": [],
                "journals": [],
                "conferences": [],
                "books": []
            },
            "misc": {
                "awards": [],
                "activities": []
            },
            "references": []
        }
        self.journal_metrics = self._load_journal_metrics()

    def _load_journal_metrics(self) -> Dict[str, Dict[str, str]]:
        """Excel 파일에서 저널 메트릭 정보를 로드"""
        excel_path = self.base_dir / "journal_pubs.xlsx"

        if not excel_path.exists():
            print(f"⚠ {excel_path} not found, journal metrics will not be available")
            return {}

        try:
            df = pd.read_excel(excel_path)
            metrics_dict = {}

            for _, row in df.iterrows():
                title = str(row.get('제목', '')).strip()
                if not title or title == 'nan':
                    continue

                # 제목을 키로 사용 (정규화: 소문자, 공백 제거)
                title_key = title.lower().replace(' ', '')

                metrics = {}

                # Impact Factor
                if pd.notna(row.get('Impact Factor')):
                    metrics['impact_factor'] = str(row['Impact Factor'])

                # JCR (percentile ranking)
                if pd.notna(row.get('JCR')):
                    jcr_val = row['JCR']
                    # Top X% 형식으로 변환
                    metrics['jcr_ranking'] = f"Top {jcr_val}%"

                # 분야
                if pd.notna(row.get('분야')):
                    metrics['jcr_field'] = str(row['분야'])

                # Rating (Q1, Q2 등)
                if pd.notna(row.get('Rating')):
                    metrics['jcr_quantile'] = str(row['Rating'])

                if metrics:
                    metrics_dict[title_key] = metrics

            print(f"✓ Loaded metrics for {len(metrics_dict)} publications from Excel")
            return metrics_dict

        except Exception as e:
            print(f"⚠ Error loading journal metrics from Excel: {e}")
            return {}

    def parse_main_file(self, main_file: str = "cv-taewon.tex"):
        """메인 TeX 파일에서 개인 정보 추출"""
        main_path = self.base_dir / main_file

        with open(main_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 이름 추출
        name_match = re.search(r'\\LARGE\\bfseries\\sffamily\s+([^,}]+)', content)
        if name_match:
            self.cv_data["personal"]["name"] = name_match.group(1).strip()

        # 이메일 추출
        email_match = re.search(r'\\href\{mailto:([^}]+)\}', content)
        if email_match:
            self.cv_data["personal"]["email"] = email_match.group(1)

        # GitHub 추출
        github_match = re.search(r'\\href\{https://github\.com/([^}]+)\}', content)
        if github_match:
            self.cv_data["personal"]["github"] = github_match.group(1)

        # LinkedIn 추출
        linkedin_match = re.search(r'\\href\{https://www\.linkedin\.com/in/([^}]+)/?\}', content)
        if linkedin_match:
            self.cv_data["personal"]["linkedin"] = linkedin_match.group(1)

        # 웹사이트 추출
        website_match = re.search(r'\\url\{(https://sites\.google\.com[^}]+)\}', content)
        if website_match:
            self.cv_data["personal"]["website"] = website_match.group(1)

        # Google Scholar 추출
        scholar_match = re.search(r'\\url\{(https://scholar\.google\.com[^}]+)\}', content)
        if scholar_match:
            self.cv_data["personal"]["scholar"] = scholar_match.group(1)

    def parse_biography(self, bio_file: str = "bio.tex"):
        """약력(Biography) 파일 파싱"""
        bio_path = self.base_dir / bio_file

        with open(bio_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # \entry*[] 다음의 텍스트 추출
        bio_match = re.search(r'\\entry\*\[\]%?\s*(.*?)\\end\{rubric\}', content, re.DOTALL)
        if bio_match:
            bio_text = bio_match.group(1).strip()
            # LaTeX 명령어 제거
            bio_text = re.sub(r'\\textbf\{([^}]+)\}', r'\1', bio_text)
            bio_text = re.sub(r'\\&', '&', bio_text)
            bio_text = re.sub(r'%.*$', '', bio_text, flags=re.MULTILINE)
            bio_text = bio_text.strip()
            self.cv_data["biography"] = bio_text

    def parse_employment(self, employment_file: str = "employment.tex"):
        """경력(Employment) 파일 파싱"""
        emp_path = self.base_dir / employment_file

        with open(emp_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 각 entry 추출
        entries = re.findall(r'\\entry\*\[([^\]]+)\]%?\s*(.*?)(?=\\entry\*|\\end\{rubric\}|%)',
                            content, re.DOTALL)

        for period, description in entries:
            # 직책과 소속 분리
            desc_clean = description.strip()
            desc_clean = re.sub(r'\\textbf\{([^}]+)\}', r'\1', desc_clean)
            desc_clean = re.sub(r'\\newline', '\n', desc_clean)

            lines = [line.strip() for line in desc_clean.split('\n') if line.strip()]

            entry = {
                "period": period.strip(),
                "position": lines[0] if len(lines) > 0 else "",
                "organization": lines[1] if len(lines) > 1 else ""
            }
            self.cv_data["employment"].append(entry)

    def parse_education(self, education_file: str = "education.tex"):
        """학력(Education) 파일 파싱"""
        edu_path = self.base_dir / education_file

        with open(edu_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 각 entry 추출
        entries = re.findall(r'\\entry\*\[([^\]]+)\]%?\s*(.*?)(?=\\entry\*|\\end\{rubric\})',
                            content, re.DOTALL)

        for period, description in entries:
            desc_clean = description.strip()
            desc_clean = re.sub(r'\\textbf\{([^}]+)\}', r'\1', desc_clean)
            desc_clean = re.sub(r'\\emph\{([^}]+)\}', r'\1', desc_clean)
            desc_clean = re.sub(r'\\par', '\n', desc_clean)

            lines = [line.strip() for line in desc_clean.split('\n') if line.strip()]

            entry = {
                "period": period.strip(),
                "degree": lines[0] if len(lines) > 0 else "",
                "thesis": lines[1].strip('"') if len(lines) > 1 and '"' in lines[1] else "",
                "advisor": lines[2].replace('Advisor: ', '') if len(lines) > 2 else ""
            }
            self.cv_data["education"].append(entry)

    def parse_skills(self, skills_file: str = "skills.tex"):
        """스킬(Skills) 파일 파싱"""
        skills_path = self.base_dir / skills_file

        with open(skills_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 각 entry 추출
        entries = re.findall(r'\\entry\*\[([^\]]+)\]\s*(.*?)(?=\\entry\*|\\end\{rubric\})',
                            content, re.DOTALL)

        for category, items in entries:
            category_clean = category.strip()
            items_clean = items.strip()
            items_clean = re.sub(r'\\ldots', '...', items_clean)

            self.cv_data["skills"][category_clean] = items_clean

    def parse_projects(self, projects_file: str = "projects.tex"):
        """프로젝트(Projects) 파일 파싱"""
        proj_path = self.base_dir / projects_file

        with open(proj_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 주석 제거 (% 시작 라인)
        content = re.sub(r'^\s*%.*$', '', content, flags=re.MULTILINE)

        # 각 entry 추출
        entries = re.findall(r'\\entry\*\[([^\]]+)\]\s*\\textbf\{([^}]+)\}[,\s]*\\newline\s*\\textbf\{([^}]+)\}[,\s]*([^\n]*)',
                            content)

        for period, title, role, funding in entries:
            entry = {
                "period": period.strip(),
                "title": title.strip(),
                "role": role.strip(),
                "funding": funding.strip()
            }
            self.cv_data["projects"].append(entry)

    def parse_publications(self, bib_file: str = "own-bib.bib"):
        """논문 목록(Publications) 파일 파싱"""
        bib_path = self.base_dir / bib_file

        try:
            with open(bib_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"⚠ {bib_file} not found, skipping publications")
            return

        # BibTeX 항목들을 @ 기준으로 분할
        # 첫 번째는 빈 문자열이므로 제외
        entries_raw = re.split(r'\n(?=@)', content)[1:] if content.startswith('\n') else re.split(r'(?=@)', content)

        for entry_raw in entries_raw:
            if not entry_raw.strip():
                continue

            # 항목 타입과 키 추출: @Type{key,
            type_match = re.match(r'@(\w+)\{([^,]+),', entry_raw)
            if not type_match:
                continue

            entry_type = type_match.group(1)
            key = type_match.group(2)

            # 필드 파싱 - 중괄호 균형 유지하면서 파싱
            field_dict = {}

            # 각 필드를 찾기: field = {value}
            # value는 중첩 괄호를 포함할 수 있음
            field_pattern = r'(\w+)\s*=\s*\{'
            field_positions = [(m.group(1), m.start(), m.end()) for m in re.finditer(field_pattern, entry_raw)]

            for i, (field_name, start, end) in enumerate(field_positions):
                # 값의 시작 위치 (= { 다음)
                value_start = end

                # 중괄호 균형을 맞춰서 값의 끝 찾기
                brace_count = 1
                pos = value_start
                while pos < len(entry_raw) and brace_count > 0:
                    if entry_raw[pos] == '{':
                        brace_count += 1
                    elif entry_raw[pos] == '}':
                        brace_count -= 1
                    pos += 1

                if brace_count == 0:
                    value = entry_raw[value_start:pos-1].strip()
                    field_dict[field_name.lower()] = value

            # 저자, 제목, 연도 추출
            title = field_dict.get('title', '').strip('{}')
            pub_entry = {
                "type": entry_type.lower(),
                "key": key,
                "title": title,
                "author": field_dict.get('author', '').replace('*', ''),  # 별표 제거
                "year": field_dict.get('year', ''),
                "journal": field_dict.get('journal', ''),
                "booktitle": field_dict.get('booktitle', ''),
                "volume": field_dict.get('volume', ''),
                "number": field_dict.get('number', ''),
                "pages": field_dict.get('pages', ''),
                "doi": field_dict.get('doi', ''),
                "url": field_dict.get('url', ''),
                "keywords": field_dict.get('keywords', ''),
                "impact_factor": field_dict.get('impact_factor', ''),
                "jcr_quantile": field_dict.get('jcr_quantile', ''),
                "jcr_ranking": field_dict.get('jcr_ranking', ''),
                "jcr_field": field_dict.get('jcr_field', '')
            }

            # Excel 파일에서 메트릭 정보 매칭 (bib 파일에 없는 경우만)
            title_key = title.lower().replace(' ', '')
            if title_key in self.journal_metrics:
                excel_metrics = self.journal_metrics[title_key]
                # bib 파일에 값이 없으면 Excel 값 사용
                if not pub_entry['impact_factor']:
                    pub_entry['impact_factor'] = excel_metrics.get('impact_factor', '')
                if not pub_entry['jcr_quantile']:
                    pub_entry['jcr_quantile'] = excel_metrics.get('jcr_quantile', '')
                if not pub_entry['jcr_ranking']:
                    pub_entry['jcr_ranking'] = excel_metrics.get('jcr_ranking', '')
                if not pub_entry['jcr_field']:
                    pub_entry['jcr_field'] = excel_metrics.get('jcr_field', '')

            # 카테고리별로 분류 (books 제외)
            if 'early access' in pub_entry['keywords'].lower():
                self.cv_data["publications"]["early_access"].append(pub_entry)
            elif entry_type.lower() == 'article':
                self.cv_data["publications"]["journals"].append(pub_entry)
            elif entry_type.lower() == 'inproceedings':
                self.cv_data["publications"]["conferences"].append(pub_entry)
            # book과 incollection은 제외

    def parse_misc(self, misc_file: str = "misc.tex"):
        """기타 경력(Miscellaneous) 파일 파싱"""
        misc_path = self.base_dir / misc_file

        try:
            with open(misc_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"⚠ {misc_file} not found, skipping miscellaneous")
            return

        # Awards 섹션 추출
        awards_match = re.search(r'\\subrubric\{Awards and Achievements\}(.*?)(?=\\subrubric|\\end\{rubric\})',
                                content, re.DOTALL)
        if awards_match:
            awards_content = awards_match.group(1)
            award_entries = re.findall(r'\\entry\*\[([^\]]+)\]\s*\\textbf\{([^}]+)\}[,\s]*\\newline\s*([^\n]+)',
                                      awards_content)

            for year, title, org in award_entries:
                self.cv_data["misc"]["awards"].append({
                    "year": year.strip(),
                    "title": title.strip(),
                    "organization": org.strip()
                })

        # Activities 섹션 추출
        activities_match = re.search(r'\\subrubric\{Activities\}(.*?)(?=\\subrubric|\\end\{rubric\})',
                                    content, re.DOTALL)
        if activities_match:
            activities_content = activities_match.group(1)
            # \entry*[year] \textbf{activity} 또는 \entry*[year] activity 패턴
            activity_entries = re.findall(r'\\entry\*\[([^\]]+)\]\s*(?:\\faLink\s*)?(?:\\href\{[^}]+\}\{)?\\textbf\{([^}]+)\}|\\entry\*\[([^\]]+)\]\s*(?:\\faLink\s*)?(?:\\href\{[^}]+\}\{)?([^\n\\]+)',
                                        activities_content)

            for match in activity_entries:
                if match[0] and match[1]:  # \textbf 패턴
                    self.cv_data["misc"]["activities"].append({
                        "year": match[0].strip(),
                        "activity": match[1].strip()
                    })
                elif match[2] and match[3]:  # 일반 텍스트 패턴
                    self.cv_data["misc"]["activities"].append({
                        "year": match[2].strip(),
                        "activity": match[3].strip()
                    })

    def parse_references(self, ref_file: str = "referee-full.tex"):
        """추천인(References) 파일 파싱"""
        ref_path = self.base_dir / ref_file

        try:
            with open(ref_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"⚠ {ref_file} not found, skipping references")
            return

        # \textbf{Name}, position\par 다음에 organization이 나오는 패턴
        # 예: \textbf{Sangheon Pack}, Professor\par
        #     School of Electrical Engineering, Korea University,\par
        ref_pattern = r'\\textbf\{([^}]+)\},\s*([^\n\\]+)\\par\s*([^\n\\]+?)(?:,)?\\par'
        ref_entries = re.findall(ref_pattern, content, re.DOTALL)

        for name, position, organization in ref_entries:
            # 이메일 추출 (해당 reference block 내에서)
            # \textbf{Name} 이후부터 다음 \textbf 또는 파일 끝까지의 영역에서 이메일 찾기
            name_escaped = re.escape(name)
            block_pattern = rf'\\textbf\{{{name_escaped}\}}.*?(?=\\textbf|\\end\{{tabularx\}}|$)'
            block_match = re.search(block_pattern, content, re.DOTALL)

            email = ""
            if block_match:
                email_match = re.search(r'\\url\{([^}]+)\}', block_match.group(0))
                if email_match:
                    email = email_match.group(1)

            ref_entry = {
                "name": name.strip(),
                "position": position.strip(),
                "organization": organization.strip(),
                "email": email
            }

            self.cv_data["references"].append(ref_entry)

    def save_to_json(self, output_file: str = "cv_data.json"):
        """JSON 파일로 저장"""
        output_path = self.base_dir / output_file

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.cv_data, f, ensure_ascii=False, indent=2)

        print(f"✓ CV 데이터가 {output_file}에 저장되었습니다.")

    def parse_all(self):
        """모든 파일 파싱"""
        print("TeX CV 파일 파싱 시작...")

        self.parse_main_file()
        print("✓ 메인 파일 (개인 정보) 파싱 완료")

        self.parse_biography()
        print("✓ 약력 파싱 완료")

        self.parse_employment()
        print("✓ 경력 파싱 완료")

        self.parse_education()
        print("✓ 학력 파싱 완료")

        self.parse_skills()
        print("✓ 스킬 파싱 완료")

        self.parse_projects()
        print("✓ 프로젝트 파싱 완료")

        self.parse_publications()
        print("✓ 논문 목록 파싱 완료")

        self.parse_misc()
        print("✓ 기타 경력 파싱 완료")

        self.parse_references()
        print("✓ 추천인 파싱 완료")

        print("\n모든 파싱 완료!")
        return self.cv_data


def main():
    """메인 함수"""
    # 스크립트가 있는 디렉토리의 상위 디렉토리를 기준으로 함
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent

    parser = TexCVParser(base_dir)
    cv_data = parser.parse_all()

    # JSON 파일로 저장
    parser.save_to_json("web/data/cv_data.json")

    # 요약 출력
    print("\n=== 파싱된 데이터 요약 ===")
    print(f"이름: {cv_data['personal'].get('name', 'N/A')}")
    print(f"이메일: {cv_data['personal'].get('email', 'N/A')}")
    print(f"경력: {len(cv_data['employment'])}개 항목")
    print(f"학력: {len(cv_data['education'])}개 항목")
    print(f"프로젝트: {len(cv_data['projects'])}개 항목")
    print(f"논문: {len(cv_data['publications']['journals'])} 저널, {len(cv_data['publications']['conferences'])} 학회")
    print(f"수상/활동: {len(cv_data['misc']['awards'])} 수상, {len(cv_data['misc']['activities'])} 활동")
    print(f"추천인: {len(cv_data['references'])}명")


if __name__ == "__main__":
    main()
