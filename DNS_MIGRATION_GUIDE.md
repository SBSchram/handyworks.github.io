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

## Step 2: DNS Configuration (Namecheap)

### Namecheap DNS Setup Instructions:

1. **Log into Namecheap:**
   - Go to https://www.namecheap.com
   - Sign in to your account
   - Go to "Domain List" → Select "handyworks.com" → Click "Manage"

2. **Choose DNS Management:**
   - Select "Advanced DNS" tab
   - You'll see current DNS records

3. **Add/Update CNAME Record for www:**
   - Click "Add New Record"
   - Select **CNAME Record**
   - **Host:** `www`
   - **Value:** `sbschram.github.io`
   - **TTL:** Automatic (or 3600)
   - Click the checkmark to save

4. **For apex domain (handyworks.com without www) - Optional:**
   - If you want both www and non-www to work:
   - Click "Add New Record"
   - Select **A Record**
   - **Host:** `@` (or leave blank)
   - **Value:** `185.199.108.153`
   - Click checkmark
   - Repeat for these IPs:
     - `185.199.109.153`
     - `185.199.110.153`
     - `185.199.111.153`

**Note:** The CNAME file is set for `www.handyworks.com`, so the www subdomain is required. The apex domain (without www) is optional but recommended.

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

