/**
 * Main JavaScript for CV Website
 * Handles dynamic content loading, dark mode, and interactivity
 */

// ===================================
// Configuration
// ===================================
const DATA_PATH = 'data/cv_data.json';
const THEME_KEY = 'cv-theme';

// ===================================
// State Management
// ===================================
let cvData = null;

// ===================================
// Initialization
// ===================================
document.addEventListener('DOMContentLoaded', async () => {
    console.log('CV Website initializing...');

    // Initialize theme
    initTheme();

    // Load CV data
    await loadCVData();

    // Render content
    renderContent();

    // Setup event listeners
    setupEventListeners();

    // Update last updated date
    updateLastUpdated();

    console.log('CV Website initialized successfully!');
});

// ===================================
// Data Loading
// ===================================
async function loadCVData() {
    try {
        const response = await fetch(DATA_PATH);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        cvData = await response.json();
        console.log('CV data loaded:', cvData);
    } catch (error) {
        console.error('Error loading CV data:', error);
        showError('Failed to load CV data. Please try refreshing the page.');
    }
}

// ===================================
// Content Rendering
// ===================================
function renderContent() {
    if (!cvData) {
        console.error('No CV data available');
        return;
    }

    renderPersonalInfo();
    renderBiography();
    renderEmployment();
    renderEducation();
    renderSkills();
    renderProjects();
    renderPublications();
    renderMiscellaneous();
    renderReferences();
}

function renderPersonalInfo() {
    const { personal } = cvData;

    // Name
    const nameEl = document.getElementById('name');
    if (nameEl) {
        nameEl.textContent = personal.name || 'Name not available';
    }

    // Email
    const emailEl = document.getElementById('email');
    if (emailEl && personal.email) {
        emailEl.href = `mailto:${personal.email}`;
        emailEl.querySelector('span').textContent = personal.email;
    }

    // GitHub
    const githubEl = document.getElementById('github');
    if (githubEl && personal.github) {
        githubEl.href = `https://github.com/${personal.github}`;
        githubEl.querySelector('span').textContent = personal.github;
    }

    // LinkedIn
    const linkedinEl = document.getElementById('linkedin');
    if (linkedinEl && personal.linkedin) {
        const linkedinId = personal.linkedin.replace(/\/$/, ''); // Remove trailing slash
        linkedinEl.href = `https://www.linkedin.com/in/${linkedinId}`;
        linkedinEl.querySelector('span').textContent = 'LinkedIn';
    }

    // Website
    const websiteEl = document.getElementById('website');
    if (websiteEl && personal.website) {
        websiteEl.href = personal.website;
        websiteEl.querySelector('span').textContent = 'Lab Website';
    }

    // Google Scholar
    const scholarEl = document.getElementById('scholar');
    if (scholarEl && personal.scholar) {
        scholarEl.href = personal.scholar;
        scholarEl.querySelector('span').textContent = 'Google Scholar';
    }
}

function renderBiography() {
    const bioEl = document.getElementById('biography');
    if (bioEl && cvData.biography) {
        bioEl.innerHTML = `<p>${cvData.biography}</p>`;
    }
}

function renderEmployment() {
    const employmentEl = document.getElementById('employment');
    if (!employmentEl || !cvData.employment) return;

    employmentEl.innerHTML = cvData.employment.map(job => `
        <div class="timeline-item">
            <div class="timeline-period">${escapeHtml(job.period)}</div>
            <div class="timeline-position">${escapeHtml(job.position)}</div>
            <div class="timeline-organization">${escapeHtml(job.organization)}</div>
        </div>
    `).join('');
}

function renderEducation() {
    const educationEl = document.getElementById('education');
    if (!educationEl || !cvData.education) return;

    educationEl.innerHTML = cvData.education.map(edu => `
        <div class="timeline-item">
            <div class="timeline-period">${escapeHtml(edu.period)}</div>
            <div class="timeline-degree">${escapeHtml(edu.degree)}</div>
            ${edu.thesis ? `<div class="timeline-thesis">"${escapeHtml(edu.thesis)}"</div>` : ''}
            ${edu.advisor ? `<div class="timeline-advisor"><strong>Advisor:</strong> ${escapeHtml(edu.advisor)}</div>` : ''}
        </div>
    `).join('');
}

function renderSkills() {
    const skillsEl = document.getElementById('skills');
    if (!skillsEl || !cvData.skills) return;

    skillsEl.innerHTML = Object.entries(cvData.skills).map(([category, items]) => `
        <div class="skill-item">
            <div class="skill-category">${escapeHtml(category)}</div>
            <div class="skill-list">${escapeHtml(items)}</div>
        </div>
    `).join('');
}

function renderProjects() {
    const projectsEl = document.getElementById('projects');
    if (!projectsEl || !cvData.projects) return;

    projectsEl.innerHTML = cvData.projects.map(project => `
        <div class="project-item">
            <div class="project-header">
                <div class="project-period">${escapeHtml(project.period)}</div>
            </div>
            <div class="project-title">${escapeHtml(project.title)}</div>
            <div class="project-role"><strong>Role:</strong> ${escapeHtml(project.role)}</div>
            <div class="project-funding"><strong>Funding:</strong> ${escapeHtml(project.funding)}</div>
        </div>
    `).join('');
}

function renderPublications() {
    if (!cvData.publications) return;

    // Render Early Access publications
    const earlyEl = document.querySelector('#publications-early .publication-list');
    const earlyCategory = document.getElementById('publications-early');
    if (earlyEl && earlyCategory) {
        if (cvData.publications.early_access && cvData.publications.early_access.length > 0) {
            const pubs = cvData.publications.early_access;
            earlyEl.innerHTML = pubs.map((pub, index) =>
                createPublicationHTML(pub, pubs.length - index)
            ).join('');
            updatePublicationCount(earlyCategory, pubs.length);
        } else {
            earlyCategory.style.display = 'none';
        }
    }

    // Render Journal articles
    const journalsEl = document.querySelector('#publications-journals .publication-list');
    const journalsCategory = document.getElementById('publications-journals');
    if (journalsEl && journalsCategory && cvData.publications.journals) {
        const pubs = cvData.publications.journals;
        journalsEl.innerHTML = pubs.map((pub, index) =>
            createPublicationHTML(pub, pubs.length - index)
        ).join('');
        updatePublicationCount(journalsCategory, pubs.length);
    }

    // Render Conference proceedings
    const conferencesEl = document.querySelector('#publications-conferences .publication-list');
    const conferencesCategory = document.getElementById('publications-conferences');
    if (conferencesEl && conferencesCategory && cvData.publications.conferences) {
        const pubs = cvData.publications.conferences;
        conferencesEl.innerHTML = pubs.map((pub, index) =>
            createPublicationHTML(pub, pubs.length - index)
        ).join('');
        updatePublicationCount(conferencesCategory, pubs.length);
    }

    // Setup collapsible functionality
    setupCollapsiblePublications();
}

function updatePublicationCount(categoryElement, count) {
    const countSpan = categoryElement.querySelector('.pub-count');
    if (countSpan) {
        countSpan.textContent = `(${count})`;
    }
}

function setupCollapsiblePublications() {
    const collapsibleHeaders = document.querySelectorAll('.publication-subtitle.collapsible-header');

    collapsibleHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const category = this.closest('.publication-category');
            category.classList.toggle('collapsed');
        });
    });
}

function normalizeAuthorName(author) {
    /**
     * 저자명을 "Firstname Lastname" 형식으로 정규화
     */
    author = author.trim();

    // 쉼표가 있으면 (Lastname, Firstname) -> (Firstname Lastname) 변환
    if (author.includes(',')) {
        const parts = author.split(',').map(p => p.trim());
        if (parts.length === 2) {
            return `${parts[1]} ${parts[0]}`;  // Firstname Lastname
        }
    }

    // 쉼표 없으면 그대로 반환 (이미 Firstname Lastname 형식)
    return author;
}

function formatAuthors(authorString) {
    /**
     * 저자 목록을 포맷팅: "저자1, 저자2, 저자3, and 저자4"
     * Taewon Song은 bold 처리
     */
    if (!authorString) return '';

    // "and"로 분리
    const authors = authorString.split(/\s+and\s+/).map(a => normalizeAuthorName(a));

    // Taewon Song을 bold 처리하는 함수
    const highlightMyName = (author) => {
        if (author === 'Taewon Song') {
            return `<strong>${author}</strong>`;
        }
        return author;
    };

    if (authors.length === 0) {
        return '';
    } else if (authors.length === 1) {
        return highlightMyName(authors[0]);
    } else if (authors.length === 2) {
        return `${highlightMyName(authors[0])} and ${highlightMyName(authors[1])}`;
    } else {
        // 3명 이상: "저자1, 저자2, 저자3, and 저자4"
        const lastAuthor = authors[authors.length - 1];
        const otherAuthors = authors.slice(0, -1);
        return `${otherAuthors.map(highlightMyName).join(', ')}, and ${highlightMyName(lastAuthor)}`;
    }
}

function createPublicationHTML(pub, number) {
    const venue = pub.journal || pub.booktitle || '';
    const volumeInfo = pub.volume ? `Vol. ${pub.volume}` : '';
    const numberInfo = pub.number ? `No. ${pub.number}` : '';
    const pagesInfo = pub.pages ? `pp. ${pub.pages}` : '';
    const venueDetails = [volumeInfo, numberInfo, pagesInfo].filter(x => x).join(', ');

    const doiLink = pub.doi ?
        (pub.doi.startsWith('http') ? pub.doi : `https://doi.org/${pub.doi}`) :
        pub.url;

    // 저자명 포맷팅 (HTML 태그 포함하므로 escape 안 함)
    const formattedAuthors = formatAuthors(pub.author);

    return `
        <div class="publication-item">
            <div class="publication-number">[${number}]</div>
            <div class="publication-content">
                <div class="publication-title">${escapeHtml(pub.title)}</div>
                <div class="publication-authors">${formattedAuthors}</div>
                <div class="publication-venue">
                    ${escapeHtml(venue)}${venueDetails ? ', ' + venueDetails : ''}
                </div>
                <div class="publication-meta">
                    <span class="publication-year">
                        <i class="fas fa-calendar"></i> ${escapeHtml(pub.year)}
                    </span>
                    ${doiLink ? `
                        <span class="publication-doi">
                            <i class="fas fa-link"></i>
                            <a href="${doiLink}" target="_blank" rel="noopener noreferrer">
                                ${pub.doi ? 'DOI' : 'Link'}
                            </a>
                        </span>
                    ` : ''}
                </div>
            </div>
        </div>
    `;
}

function renderMiscellaneous() {
    if (!cvData.misc) return;

    // Render Awards
    const awardsEl = document.getElementById('awards');
    if (awardsEl && cvData.misc.awards) {
        awardsEl.innerHTML = cvData.misc.awards.map(award => `
            <div class="award-item">
                <div class="award-year">${escapeHtml(award.year)}</div>
                <div class="award-content">
                    <div class="award-title">${escapeHtml(award.title)}</div>
                    <div class="award-org">${escapeHtml(award.organization)}</div>
                </div>
            </div>
        `).join('');
    }

    // Render Activities
    const activitiesEl = document.getElementById('activities');
    if (activitiesEl && cvData.misc.activities) {
        activitiesEl.innerHTML = cvData.misc.activities.map(activity => `
            <div class="activity-item">
                <div class="activity-year">${escapeHtml(activity.year)}</div>
                <div class="activity-content">
                    <div class="activity-title">${escapeHtml(activity.activity)}</div>
                </div>
            </div>
        `).join('');
    }
}

function renderReferences() {
    const referencesEl = document.getElementById('references');
    if (!referencesEl || !cvData.references) return;

    referencesEl.innerHTML = cvData.references.map(ref => `
        <div class="reference-item">
            <div class="reference-name">${escapeHtml(ref.name)}</div>
            <div class="reference-position">${escapeHtml(ref.position)}</div>
            ${ref.organization ? `<div class="reference-org">${escapeHtml(ref.organization)}</div>` : ''}
            ${ref.email ? `
                <a href="mailto:${ref.email}" class="reference-email">
                    <i class="fas fa-envelope"></i>
                    ${escapeHtml(ref.email)}
                </a>
            ` : ''}
        </div>
    `).join('');
}

// ===================================
// Theme Management
// ===================================
function initTheme() {
    const savedTheme = localStorage.getItem(THEME_KEY);
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    const theme = savedTheme || (prefersDark ? 'dark' : 'light');
    setTheme(theme);
}

function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem(THEME_KEY, theme);

    // Update toggle button icon
    const toggleBtn = document.getElementById('darkModeToggle');
    if (toggleBtn) {
        const icon = toggleBtn.querySelector('i');
        if (theme === 'dark') {
            icon.className = 'fas fa-sun';
        } else {
            icon.className = 'fas fa-moon';
        }
    }
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
}

// ===================================
// Event Listeners
// ===================================
function setupEventListeners() {
    // Dark mode toggle
    const darkModeToggle = document.getElementById('darkModeToggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', toggleTheme);
    }

    // Print button
    const printButton = document.getElementById('printButton');
    if (printButton) {
        printButton.addEventListener('click', () => {
            window.print();
        });
    }

    // PDF download button (will be configured by GitHub Actions)
    const pdfDownload = document.getElementById('pdfDownload');
    if (pdfDownload) {
        // Check if PDF exists
        pdfDownload.href = '../cv-taewon.pdf';
        pdfDownload.addEventListener('click', (e) => {
            // Could add analytics or confirmation here
            console.log('PDF download clicked');
        });
    }

    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem(THEME_KEY)) {
            setTheme(e.matches ? 'dark' : 'light');
        }
    });

    // Smooth scroll for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// ===================================
// Utility Functions
// ===================================
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;',
        '\\': '' // Remove LaTeX escape characters
    };
    return String(text).replace(/[&<>"'\\]/g, m => map[m]);
}

function updateLastUpdated() {
    const lastUpdatedEl = document.getElementById('lastUpdated');
    if (lastUpdatedEl) {
        const now = new Date();
        const options = {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        };
        lastUpdatedEl.textContent = now.toLocaleDateString('en-US', options);
    }
}

function showError(message) {
    const container = document.querySelector('.container');
    if (container) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.style.cssText = `
            background-color: #f8d7da;
            color: #721c24;
            padding: 1rem;
            margin: 1rem 0;
            border: 1px solid #f5c6cb;
            border-radius: 8px;
            text-align: center;
        `;
        errorDiv.textContent = message;
        container.insertBefore(errorDiv, container.firstChild);
    }
}

// ===================================
// Keyboard Shortcuts
// ===================================
document.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + P for print
    if ((e.ctrlKey || e.metaKey) && e.key === 'p') {
        e.preventDefault();
        window.print();
    }

    // Ctrl/Cmd + D for dark mode toggle
    if ((e.ctrlKey || e.metaKey) && e.key === 'd') {
        e.preventDefault();
        toggleTheme();
    }
});

// ===================================
// Analytics (Optional)
// ===================================
function trackEvent(category, action, label) {
    // If you add Google Analytics or other analytics
    if (typeof gtag !== 'undefined') {
        gtag('event', action, {
            'event_category': category,
            'event_label': label
        });
    }
    console.log(`Analytics: ${category} - ${action} - ${label}`);
}

// ===================================
// Service Worker Registration (Optional - for PWA)
// ===================================
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        // Uncomment to enable service worker for offline support
        // navigator.serviceWorker.register('/sw.js')
        //     .then(registration => console.log('SW registered:', registration))
        //     .catch(error => console.log('SW registration failed:', error));
    });
}

// ===================================
// Export for testing (if needed)
// ===================================
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        loadCVData,
        renderContent,
        toggleTheme,
        escapeHtml
    };
}
