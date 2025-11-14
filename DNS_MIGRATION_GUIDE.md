# DNS Migration Guide for HandyWorks Website

## Overview
This guide will help you migrate the `handyworks.com` domain from WordPress hosting to GitHub Pages.

## Current Status
- ✅ Site is live on GitHub Pages: `https://sbschram.github.io/handyworks-website/`
- ✅ CNAME file created: `www.handyworks.com`
- ⏳ Waiting for DNS configuration

## Step 1: GitHub Pages Custom Domain Setup

### In GitHub Repository:
1. Go to: `https://github.com/SBSchram/handyworks-website/settings/pages`
2. Under "Custom domain", enter: `www.handyworks.com`
3. Check "Enforce HTTPS" (after DNS propagates)
4. GitHub will automatically create/update the CNAME file

**Note:** The CNAME file has been created in the repository with `www.handyworks.com`

## Step 2: DNS Configuration

You need to add/update DNS records at your domain registrar (where handyworks.com is registered).

### Required DNS Records:

#### Option A: Using www subdomain (Recommended)
```
Type: CNAME
Name: www
Value: sbschram.github.io
TTL: 3600 (or default)
```

#### Option B: Using apex domain (handyworks.com without www)
```
Type: A
Name: @ (or blank)
Value: 185.199.108.153
Value: 185.199.109.153
Value: 185.199.110.153
Value: 185.199.111.153
```

**Note:** GitHub Pages supports both www and apex domains. The CNAME file is set for `www.handyworks.com`.

### DNS Propagation
- DNS changes can take 24-48 hours to propagate globally
- You can check propagation status at: https://www.whatsmydns.net/#CNAME/www.handyworks.com

## Step 3: Verify Domain

After DNS propagates:
1. GitHub will automatically detect the domain
2. SSL certificate will be provisioned (takes a few minutes to hours)
3. You can enable "Enforce HTTPS" in GitHub Pages settings

## Step 4: Test the Site

Once DNS is configured and SSL is active:
- Test: `https://www.handyworks.com`
- Verify all pages load correctly
- Test downloads from `public/` directory
- Test desktop software version check: `https://www.handyworks.com/public/LatestVersion.txt`

## Important URLs After Migration

- **Main site:** `https://www.handyworks.com`
- **Blog:** `https://www.handyworks.com/` (homepage)
- **Downloads:** `https://www.handyworks.com/downloads.html`
- **LatestVersion.txt:** `https://www.handyworks.com/public/LatestVersion.txt`
- **Upgrade file:** `https://www.handyworks.com/public/HW_Upgrade_2_25.exe`

## Rollback Plan

If something goes wrong:
1. Remove custom domain from GitHub Pages settings
2. Revert DNS records to point back to WordPress hosting
3. Site will remain accessible at `https://sbschram.github.io/handyworks-website/`

## Current WordPress Site

**IMPORTANT:** Keep the WordPress site running until:
- DNS migration is complete
- New site is fully tested
- All functionality verified
- Desktop software can access LatestVersion.txt

## Checklist

- [ ] CNAME file created in repository ✅
- [ ] GitHub Pages custom domain configured
- [ ] DNS records added at domain registrar
- [ ] Wait for DNS propagation (24-48 hours)
- [ ] SSL certificate provisioned by GitHub
- [ ] Test www.handyworks.com
- [ ] Test all pages and downloads
- [ ] Test desktop software version check
- [ ] Verify LatestVersion.txt is accessible
- [ ] Update any hardcoded URLs if needed
- [ ] Monitor for 1-2 weeks before shutting down WordPress

## Support

If you encounter issues:
- GitHub Pages documentation: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site
- Check DNS propagation: https://www.whatsmydns.net
- GitHub Pages status: https://www.githubstatus.com

