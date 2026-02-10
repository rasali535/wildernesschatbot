/**
 * Configuration for Wilderness Destinations Chatbot
 * Update API_URL based on your deployment environment
 */

const CONFIG = {
    // For local development
    // API_URL: 'http://localhost:5000/api',

    // For Hostinger deployment with backend on subdomain
    // API_URL: 'https://api.yourdomain.com/api',

    // For Hostinger deployment with backend on same domain
    API_URL: 'https://yourdomain.com/api',

    // Chat widget settings
    WIDGET_POSITION: 'bottom-right',
    THEME: 'wilderness',

    // Session settings
    SESSION_TIMEOUT: 30 * 60 * 1000, // 30 minutes

    // Feature flags
    ENABLE_ANALYTICS: false,
    ENABLE_QUICK_REPLIES: true,
    ENABLE_TYPING_INDICATOR: true,
};

// Auto-detect environment
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    CONFIG.API_URL = 'http://localhost:5000/api';
}
