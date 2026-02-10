/**
 * Configuration for Wilderness Destinations Chatbot
 * Update API_URL based on your deployment environment
 */

const CONFIG = {
    // START HERE: This is the URL for your LIVE backend on Render
    API_URL: 'https://wildernesschatbot.onrender.com',

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

// Optional: Override for local testing if running backend locally
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    // Uncomment the line below to test with local backend instead of Render
    CONFIG.API_URL = 'http://localhost:5000/api';
    console.log('🚧 Running locally. Connecting to:', CONFIG.API_URL);
}
