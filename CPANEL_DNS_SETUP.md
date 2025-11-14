# cPanel DNS Setup for HandyWorks Website

## Current Situation
Your DNS is currently managed by cPanel (your hosting provider), not Namecheap. You can add the GitHub Pages DNS records directly in cPanel.

## Step 1: Access cPanel DNS Zone Editor

1. Log into your cPanel account (the same one you used to download WordPress backups)
2. Look for "Zone Editor" or "DNS Zone Editor" in cPanel
3. Click on it
4. Select the domain: `handyworks.com`

## Step 2: Add CNAME Record for www

1. In the Zone Editor, look for "Add Record" or "Add" button
2. Select **CNAME** from the record type dropdown
3. Fill in:
   - **Name:** `www`
   - **TTL:** `3600` (or leave default)
   - **Record:** `sbschram.github.io`
4. Click "Add Record" or "Save"

## Step 3: (Optional) Add A Records for Apex Domain

If you want `handyworks.com` (without www) to also work:

1. Click "Add Record" again
2. Select **A** from the record type dropdown
3. Fill in:
   - **Name:** `@` (or leave blank for root domain)
   - **TTL:** `3600`
   - **Address:** `185.199.108.153`
4. Click "Add Record"
5. Repeat 3 more times with these IPs:
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`

## Step 4: Verify Records

After adding, you should see:
- A CNAME record: `www` → `sbschram.github.io`
- (Optional) 4 A records: `@` → GitHub IP addresses

## Step 5: Configure GitHub Pages

1. Go to: https://github.com/SBSchram/handyworks-website/settings/pages
2. Under "Custom domain", enter: `www.handyworks.com`
3. Click "Save"
4. GitHub will show "DNS check in progress" - this is normal

## Step 6: Wait for DNS Propagation

- DNS changes typically take 1-24 hours
- Check status: https://www.whatsmydns.net/#CNAME/www.handyworks.com
- Once DNS shows `sbschram.github.io`, GitHub will provision SSL

## Step 7: Enable HTTPS

After DNS propagates:
1. Go back to GitHub Pages settings
2. Check "Enforce HTTPS"
3. SSL will be active within minutes

## Alternative: Switch DNS to Namecheap

If you prefer to manage DNS through Namecheap instead of cPanel:

1. In Namecheap, go to Domain List → handyworks.com → Manage
2. Click "Advanced DNS" tab
3. Look for "Change DNS Type" or similar option
4. Switch from "cPanel DNS" to "Namecheap BasicDNS"
5. Wait a few minutes for the change to take effect
6. Then follow the Namecheap DNS setup instructions

**Note:** Switching DNS providers can cause temporary downtime. It's usually easier to just add the records in cPanel.

