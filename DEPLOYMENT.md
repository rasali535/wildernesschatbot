# 🚀 Production Deployment Guide

## Overview

This guide covers deploying the Wilderness Destinations Chatbot to production, including integration with the actual wildernessdestinations.com website.

## 🎯 Pre-Deployment Checklist

### Backend Requirements

- [ ] Replace mock camp data with real API integration
- [ ] Implement web scraping for live camp data
- [ ] Add authentication and API keys
- [ ] Set up rate limiting
- [ ] Configure CORS for production domain
- [ ] Add comprehensive logging
- [ ] Implement error tracking (Sentry, etc.)
- [ ] Set up monitoring (New Relic, DataDog, etc.)
- [ ] Add database for conversation history
- [ ] Implement caching (Redis)
- [ ] Set up backup and recovery

### Frontend Requirements

- [ ] Update API endpoint to production URL
- [ ] Minify CSS and JavaScript
- [ ] Optimize images
- [ ] Add analytics (Google Analytics, Mixpanel)
- [ ] Implement A/B testing framework
- [ ] Add error boundaries
- [ ] Set up CDN for static assets
- [ ] Configure service worker for offline support
- [ ] Add meta tags for SEO
- [ ] Implement schema.org markup

### Security

- [ ] HTTPS/SSL certificate
- [ ] Input sanitization
- [ ] XSS prevention
- [ ] CSRF protection
- [ ] SQL injection prevention (if using database)
- [ ] Rate limiting per IP
- [ ] DDoS protection
- [ ] Security headers (CSP, HSTS, etc.)
- [ ] Regular security audits
- [ ] Dependency vulnerability scanning

### Compliance

- [ ] GDPR compliance (EU users)
- [ ] Cookie consent
- [ ] Privacy policy
- [ ] Terms of service
- [ ] Data retention policy
- [ ] Right to be forgotten implementation

## 🏗️ Architecture Options

### Option 1: Serverless (Recommended for MVP)

**Backend:**

- AWS Lambda + API Gateway
- Or Google Cloud Functions
- Or Azure Functions

**Frontend:**

- Cloudflare Pages
- Or Netlify
- Or Vercel

**Database:**

- DynamoDB (AWS)
- Or Firestore (Google)
- Or CosmosDB (Azure)

**Advantages:**

- Auto-scaling
- Pay-per-use
- Low maintenance
- High availability

### Option 2: Container-Based

**Backend:**

- Docker container
- Kubernetes cluster
- Or AWS ECS/Fargate

**Frontend:**

- Static hosting on S3 + CloudFront
- Or similar on GCP/Azure

**Database:**

- PostgreSQL (RDS, Cloud SQL)
- Redis for caching

**Advantages:**

- More control
- Better for complex workflows
- Easier local development

### Option 3: Traditional Server

**Backend:**

- VPS (DigitalOcean, Linode)
- Nginx reverse proxy
- Gunicorn/uWSGI

**Frontend:**

- Same server or separate CDN

**Advantages:**

- Simple setup
- Lower cost for low traffic
- Full control

## 📦 Deployment Steps

### Step 1: Prepare Backend for Production

Create `backend/config.py`:

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    API_KEY = os.environ.get('WILDERNESS_API_KEY')
    DATABASE_URL = os.environ.get('DATABASE_URL')
    REDIS_URL = os.environ.get('REDIS_URL')
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', 'https://wildernessdestinations.com').split(',')
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    SENTRY_DSN = os.environ.get('SENTRY_DSN')
```

Update `backend/app.py`:

```python
from config import Config
import logging
import sentry_sdk

# Initialize Sentry
sentry_sdk.init(dsn=Config.SENTRY_DSN)

# Configure logging
logging.basicConfig(level=Config.LOG_LEVEL)

# Update CORS
CORS(app, origins=Config.CORS_ORIGINS)
```

### Step 2: Create Production Requirements

`backend/requirements-prod.txt`:

```
flask==3.0.0
flask-cors==4.0.0
gunicorn==21.2.0
psycopg2-binary==2.9.9
redis==5.0.1
sentry-sdk==1.39.1
python-dotenv==1.0.0
requests==2.31.0
beautifulsoup4==4.12.2
```

### Step 3: Create Dockerfile

`backend/Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements-prod.txt .
RUN pip install --no-cache-dir -r requirements-prod.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
```

### Step 4: Create Docker Compose (for testing)

`docker-compose.yml`:

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/wilderness
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=wilderness
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

### Step 5: Deploy to AWS (Example)

**Using AWS Elastic Beanstalk:**

1. Install EB CLI:

```bash
pip install awsebcli
```

1. Initialize:

```bash
cd backend
eb init -p python-3.11 wilderness-chatbot
```

1. Create environment:

```bash
eb create wilderness-chatbot-prod
```

1. Set environment variables:

```bash
eb setenv SECRET_KEY=your-secret-key \
  WILDERNESS_API_KEY=your-api-key \
  DATABASE_URL=your-db-url
```

1. Deploy:

```bash
eb deploy
```

### Step 6: Deploy Frontend

**Using Cloudflare Pages:**

1. Update `frontend/chatbot.js`:

```javascript
this.apiUrl = 'https://api.wildernessdestinations.com/api';
```

1. Build assets (if using bundler):

```bash
npm run build
```

1. Deploy to Cloudflare:

```bash
npx wrangler pages publish frontend
```

### Step 7: Configure DNS

Add DNS records:

```
api.wildernessdestinations.com -> Backend server IP/Load balancer
chat.wildernessdestinations.com -> Frontend CDN
```

## 🔗 Integration with wildernessdestinations.com

### Option A: Embedded Widget (Recommended)

Add to their website's footer:

```html
<!-- Wilderness Chatbot Widget -->
<link rel="stylesheet" href="https://chat.wildernessdestinations.com/widget.css">
<script src="https://chat.wildernessdestinations.com/widget.js"></script>
<script>
  WildernessChatbot.init({
    apiUrl: 'https://api.wildernessdestinations.com/api',
    position: 'bottom-right',
    theme: 'wilderness'
  });
</script>
```

### Option B: Standalone Page

Create a dedicated page:

```
https://wildernessdestinations.com/safari-specialist
```

### Option C: Modal Integration

Trigger from existing "Contact" or "Enquire" buttons:

```javascript
document.querySelector('.enquire-btn').addEventListener('click', () => {
  WildernessChatbot.open();
});
```

## 📊 Monitoring & Analytics

### Key Metrics to Track

**Engagement:**

- Chat widget open rate
- Messages per session
- Session duration
- Bounce rate

**Performance:**

- API response time
- Error rate
- Uptime
- Page load time

**Business:**

- Enquiry conversion rate
- Popular destinations
- Common questions
- Lead quality

### Tools

**Analytics:**

- Google Analytics 4
- Mixpanel
- Amplitude

**Monitoring:**

- New Relic
- DataDog
- Prometheus + Grafana

**Error Tracking:**

- Sentry
- Rollbar
- Bugsnag

**Uptime:**

- Pingdom
- UptimeRobot
- StatusCake

## 🔄 CI/CD Pipeline

### GitHub Actions Example

`.github/workflows/deploy.yml`:

```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r backend/requirements-prod.txt
      - run: python -m pytest backend/tests/

  deploy-backend:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to AWS
        run: |
          pip install awsebcli
          eb deploy wilderness-chatbot-prod

  deploy-frontend:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to Cloudflare
        run: npx wrangler pages publish frontend
        env:
          CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
```

## 🎛️ Environment Variables

### Production Environment

```bash
# Backend
SECRET_KEY=your-secret-key-here
WILDERNESS_API_KEY=your-api-key
DATABASE_URL=postgresql://user:pass@host:5432/db
REDIS_URL=redis://host:6379
CORS_ORIGINS=https://wildernessdestinations.com,https://www.wildernessdestinations.com
LOG_LEVEL=INFO
SENTRY_DSN=https://your-sentry-dsn
FLASK_ENV=production

# Frontend
VITE_API_URL=https://api.wildernessdestinations.com/api
VITE_GA_ID=G-XXXXXXXXXX
```

## 🧪 Pre-Launch Testing

### Load Testing

```bash
# Using Apache Bench
ab -n 1000 -c 100 https://api.wildernessdestinations.com/api/health

# Using Locust
locust -f tests/load_test.py --host=https://api.wildernessdestinations.com
```

### Security Scan

```bash
# OWASP ZAP
zap-cli quick-scan https://chat.wildernessdestinations.com

# SSL Test
ssllabs-scan --host=api.wildernessdestinations.com
```

### Performance Audit

```bash
# Lighthouse
lighthouse https://chat.wildernessdestinations.com --output=html

# WebPageTest
webpagetest test https://chat.wildernessdestinations.com
```

## 📋 Launch Checklist

### Week Before Launch

- [ ] Complete security audit
- [ ] Load testing passed
- [ ] Backup procedures tested
- [ ] Monitoring dashboards set up
- [ ] Alert rules configured
- [ ] Documentation complete
- [ ] Team training completed

### Day Before Launch

- [ ] Final code review
- [ ] Database migrations tested
- [ ] Rollback plan ready
- [ ] Support team briefed
- [ ] Stakeholders notified

### Launch Day

- [ ] Deploy to production
- [ ] Verify all endpoints
- [ ] Check monitoring
- [ ] Test from multiple locations
- [ ] Verify analytics tracking
- [ ] Monitor error rates
- [ ] Check performance metrics

### Week After Launch

- [ ] Review analytics
- [ ] Address any issues
- [ ] Gather user feedback
- [ ] Optimize based on data
- [ ] Plan next iteration

## 🆘 Rollback Procedure

If issues arise:

1. **Immediate:**

```bash
eb deploy --version previous-version
```

1. **Database:**

```bash
# Rollback migration
alembic downgrade -1
```

1. **Frontend:**

```bash
# Revert to previous deployment
cloudflare pages deployment rollback
```

## 📞 Support

### Escalation Path

1. **Level 1:** Chatbot auto-responses
2. **Level 2:** Human safari specialists
3. **Level 3:** Technical support team
4. **Level 4:** Development team

### On-Call Rotation

- Set up PagerDuty or similar
- 24/7 coverage for critical issues
- Response time SLA: < 15 minutes

---

**Ready for Launch! 🚀🌍**
