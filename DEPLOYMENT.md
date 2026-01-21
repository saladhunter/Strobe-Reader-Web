# Deployment Guide

Your Strobe Reader web app is ready to deploy! Choose your preferred platform.

## Option 1: Railway (Recommended - Simplest)

**Pros:** Free tier, GitHub integration, auto-deploys on push

1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub"
3. Select `saladhunter/Strobe-Reader-Web`
4. Railway auto-detects Flask
5. **Done!** Your app is live in ~2 minutes

**Your app URL:** `https://strobereaderweb-production.up.railway.app` (auto-generated)

## Option 2: Render

**Pros:** Free tier, GitHub integration, good for beginners

1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Connect GitHub account
4. Select repository
5. Fill in:
   - **Name:** `strobe-reader-web`
   - **Runtime:** Python
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `python app.py`
6. **Done!** Live in ~5 minutes

## Option 3: Heroku (Free tier ending soon)

Heroku phased out free tier, but you can still use paid plans or try alternatives above.

## After Deployment

Once deployed:

1. **Test the live app** - Paste text and speed read
2. **Share the URL** - Anyone can access it (no installation needed)
3. **Push updates** - Any push to `main` branch auto-deploys

## Environment Variables

If you need to add environment variables (database URLs, API keys, etc.):

### Railway
1. Project Settings → Variables
2. Add key-value pairs

### Render
1. Environment → Environment Variables
2. Add key-value pairs

Currently no env variables needed!

## Troubleshooting

**App won't start?**
- Check logs in Railway/Render dashboard
- Verify `requirements.txt` is correct
- Test locally: `python app.py`

**Page shows 404?**
- Make sure you're visiting the root URL (not `/api/` directly)
- Check `templates/index.html` is being served

**CORS/API errors?**
- Both Railway and Render allow local and remote requests
- No additional configuration needed

## Cost

- **Railway:** Free tier includes $5/month credit (plenty for this app)
- **Render:** Free tier with limited resources (works fine for speed reading)
- **Heroku:** ~$7/month for hobby dyno (or use alternatives above)

## Next Steps

1. Deploy to Railway/Render
2. Share the live URL
3. Add features based on user feedback
4. Consider moving web version to main `Strobe-Reader` repository eventually
