# Namecheap DNS Setup for HandyWorks Website

## Quick Setup Guide

### Step 1: Access Namecheap DNS Settings

1. Go to https://www.namecheap.com and sign in
2. Click "Domain List" in the left sidebar
3. Find `handyworks.com` and click "Manage"
4. Click the "Advanced DNS" tab

### Step 2: Add CNAME Record for www

1. In the "Host Records" section, click "Add New Record"
2. Select **CNAME Record** from the dropdown
3. Fill in:
   - **Type:** CNAME Record
   - **Host:** `www`
   - **Value:** `sbschram.github.io`
   - **TTL:** Automatic (or 3600)
4. Click the checkmark (✓) to save

### Step 3: Add A Records for Apex Domain (Optional but Recommended)

To make both `www.handyworks.com` and `handyworks.com` work, add these A records:

1. Click "Add New Record" → Select **A Record**
   - **Host:** `@` (or leave blank)
   - **Value:** `185.199.108.153`
   - **TTL:** Automatic
   - Click ✓

2. Repeat 3 more times with these IPs:
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`

### Step 4: Remove Old Records (If Any)

If you see old A records or CNAME records pointing to WordPress hosting, you can remove them after the new site is working.

### Step 5: Verify in GitHub

1. Go to: https://github.com/SBSchram/handyworks-website/settings/pages
2. Under "Custom domain", enter: `www.handyworks.com`
3. Click "Save"
4. GitHub will show "DNS check in progress" - this is normal

### Step 6: Wait for DNS Propagation

- DNS changes typically take 1-24 hours to propagate
- Check status: https://www.whatsmydns.net/#CNAME/www.handyworks.com
- Once DNS shows `sbschram.github.io`, GitHub will provision SSL

### Step 7: Enable HTTPS

After DNS propagates (usually within 24 hours):
1. Go back to GitHub Pages settings
2. You'll see "Your site is ready to be published at www.handyworks.com"
3. Check the box "Enforce HTTPS"
4. SSL certificate will be active within minutes

## Testing After DNS Propagates

Once DNS is active, test these URLs:

- ✅ Main site: `https://www.handyworks.com`
- ✅ Blog: `https://www.handyworks.com/`
- ✅ Downloads: `https://www.handyworks.com/downloads.html`
- ✅ LatestVersion.txt: `https://www.handyworks.com/public/LatestVersion.txt`
- ✅ Upgrade file: `https://www.handyworks.com/public/HW_Upgrade_2_25.exe`

## Important Notes

- **Keep WordPress site running** until new site is fully tested
- The desktop software reads: `https://www.handyworks.com/public/LatestVersion.txt`
- All `public/` files will be accessible at the same paths
- DNS propagation can take up to 48 hours (usually much faster)

## Troubleshooting

**If DNS doesn't propagate:**
- Double-check the CNAME record value: `sbschram.github.io` (no trailing slash)
- Make sure Host is exactly `www` (not `www.handyworks.com`)
- Wait at least 1 hour before checking again

**If GitHub shows DNS error:**
- This is normal immediately after adding DNS records
- Wait for DNS to propagate (check with whatsmydns.net)
- GitHub will automatically detect once DNS is active

