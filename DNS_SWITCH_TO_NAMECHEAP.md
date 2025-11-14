# Switching DNS from cPanel to Namecheap & Email Forwarding Setup

## Overview
You're moving DNS management from cPanel (DNS1.TRKHOSTING.COM) to Namecheap BasicDNS, and need to set up email forwarding.

## Step 1: Switch DNS to Namecheap BasicDNS

### In Namecheap:
1. Go to https://www.namecheap.com and sign in
2. Click "Domain List" in the left sidebar
3. Find `handyworks.com` and click "Manage"
4. Click the "Advanced DNS" tab
5. Look for "Change DNS Type" or "Nameservers" section
6. Click "Change" next to the current nameservers
7. Select "Namecheap BasicDNS" (or "Namecheap Default Nameservers")
8. Click "Save" or "Update"

**Note:** This change can take 24-48 hours to fully propagate, but usually happens within a few hours.

## Step 2: Wait for DNS to Switch

- Wait 1-2 hours after making the change
- Check if DNS has switched: https://www.whatsmydns.net/#NS/handyworks.com
- You should see Namecheap nameservers (usually `dns1.registrar-servers.com` or similar)

## Step 3: Add GitHub Pages DNS Records

Once DNS has switched to Namecheap:

1. Go back to Namecheap → Domain List → handyworks.com → Manage → Advanced DNS
2. You should now see "Host Records" section (not the cPanel message)

### Add CNAME for www:
1. Click "Add New Record"
2. Select **CNAME Record**
3. Fill in:
   - **Host:** `www`
   - **Value:** `sbschram.github.io`
   - **TTL:** Automatic (or 3600)
4. Click the checkmark (✓) to save

### Add A Records for apex domain (optional but recommended):
1. Click "Add New Record" → Select **A Record**
   - **Host:** `@` (or leave blank)
   - **Value:** `185.199.108.153`
   - **TTL:** Automatic
   - Click ✓
2. Repeat 3 more times with these IPs:
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`

## Step 4: Set Up Email Forwarding in Namecheap

Namecheap offers free email forwarding for domains registered with them.

### Option A: Namecheap Email Forwarding (Free)

1. In Namecheap, go to Domain List → handyworks.com → Manage
2. Click "Email Forwarding" tab (or look for "Email" section)
3. Click "Add Forwarder" or "Create Email Address"
4. Set up your email forwards:
   - **Forward From:** `info@handyworks.com` (or whatever addresses you need)
   - **Forward To:** Your actual email address (e.g., `yourname@gmail.com`)
5. Repeat for each email address you need to forward

**Common email forwards:**
- `info@handyworks.com` → your personal email
- `contact@handyworks.com` → your personal email
- `support@handyworks.com` → your personal email
- `admin@handyworks.com` → your personal email

### Option B: Professional Email Service (Paid)

If you need more features (mailbox storage, sending emails, etc.):

**Recommended Services:**
- **Google Workspace** (~$6/month per user) - Professional Gmail
- **Microsoft 365** (~$6/month per user) - Outlook email
- **Zoho Mail** (Free tier available) - Good free option
- **ProtonMail** - Privacy-focused option

## Step 5: Configure GitHub Pages

1. Go to: https://github.com/SBSchram/handyworks-website/settings/pages
2. Under "Custom domain", enter: `www.handyworks.com`
3. Click "Save"
4. GitHub will show "DNS check in progress" - wait for DNS to propagate

## Step 6: Wait for DNS Propagation

- DNS changes can take 24-48 hours to fully propagate
- Check GitHub Pages DNS: https://www.whatsmydns.net/#CNAME/www.handyworks.com
- Once DNS shows `sbschram.github.io`, GitHub will provision SSL

## Step 7: Enable HTTPS

After DNS propagates:
1. Go back to GitHub Pages settings
2. Check "Enforce HTTPS"
3. SSL will be active within minutes

## Important Notes

### Email During Transition:
- **Before DNS switch:** Email forwarding continues working through cPanel
- **During DNS switch (1-48 hours):** Email may be temporarily unavailable
- **After DNS switch:** Email forwarding works through Namecheap

### Testing Email Forwarding:
- After setting up forwarding in Namecheap, test by sending an email to `info@handyworks.com` (or your forwarded address)
- It should arrive at your destination email within a few minutes

### If You Need to Send Emails:
- Namecheap email forwarding is **receive-only** (you can't send FROM those addresses)
- To send emails FROM `@handyworks.com`, you'll need:
  - Google Workspace
  - Microsoft 365
  - Zoho Mail
  - Or another email service

## Checklist

- [ ] Switch DNS to Namecheap BasicDNS
- [ ] Wait for DNS to propagate (1-24 hours)
- [ ] Add CNAME record for www → sbschram.github.io
- [ ] Add A records for apex domain (optional)
- [ ] Set up email forwarding in Namecheap
- [ ] Test email forwarding
- [ ] Configure GitHub Pages custom domain
- [ ] Wait for GitHub Pages DNS to propagate
- [ ] Enable HTTPS in GitHub Pages
- [ ] Test website: https://www.handyworks.com
- [ ] Test email forwarding

## Support

- Namecheap Email Forwarding: https://www.namecheap.com/support/knowledgebase/article.aspx/9247/2210/how-to-set-up-email-forwarding/
- Namecheap DNS Management: https://www.namecheap.com/support/knowledgebase/article.aspx/767/10/how-to-change-dns-for-a-domain/

