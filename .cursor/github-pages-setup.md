# GitHub Pages Setup & DNS Migration Plan

**Status:** Ready for GitHub Pages deployment  
**Current Site:** WordPress (handyworks.com) - Still Live  
**Test Site:** GitHub Pages - Ready for Testing

---

## Phase 1: GitHub Pages Setup (Current)

### Step 1: Commit and Push All Changes

```bash
# Stage all changes
git add .

# Commit
git commit -m "Complete WordPress migration: organized structure, generated HTML, cleaned up files"

# Push to GitHub
git push origin main
```

### Step 2: Configure GitHub Pages

1. Go to GitHub repository: `https://github.com/SBSchram/handyworks-website`
2. Click **Settings** → **Pages**
3. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**

### Step 3: Test on GitHub Pages URL

- **Test URL:** `https://sbschram.github.io/handyworks-website/`
- Test all pages, links, downloads, images
- Verify blog posts load correctly
- Check newsletter archive
- Test downloads

**Note:** The old WordPress site at `handyworks.com` will remain live during testing.

---

## Phase 2: DNS Migration (After Testing)

### Current DNS Setup
- **Domain:** handyworks.com
- **Current Hosting:** WordPress (cPanel)
- **CNAME Record:** Points to WordPress server

### Migration Steps

#### 1. Get GitHub Pages IP/CNAME
- GitHub Pages provides a CNAME target
- Usually: `sbschram.github.io` (for user pages)
- Or custom domain setup in GitHub Pages settings

#### 2. Update DNS Records

**In cPanel or Domain Registrar:**

1. **Option A: CNAME Record (Recommended)**
   - Type: CNAME
   - Name: `www` (or `@` for root domain)
   - Value: `sbschram.github.io.` (note the trailing dot)
   - TTL: 3600 (or default)

2. **Option B: A Records (If CNAME not supported for root)**
   - Type: A
   - Name: `@`
   - Value: GitHub Pages IP addresses:
     - 185.199.108.153
     - 185.199.109.153
     - 185.199.110.153
     - 185.199.111.153
   - TTL: 3600

3. **For www subdomain:**
   - Type: CNAME
   - Name: `www`
   - Value: `sbschram.github.io.`

#### 3. Configure Custom Domain in GitHub

1. Go to repository **Settings** → **Pages**
2. Under **Custom domain**, enter: `handyworks.com`
3. Check **Enforce HTTPS** (after DNS propagates)
4. GitHub will create a CNAME file automatically

#### 4. Wait for DNS Propagation

- DNS changes can take 24-48 hours to fully propagate
- Check propagation: `dig handyworks.com` or use online tools
- Test: `curl -I https://handyworks.com`

#### 5. Verify SSL Certificate

- GitHub Pages automatically provisions SSL via Let's Encrypt
- Wait 24-48 hours after DNS propagation
- Check SSL: `https://www.ssllabs.com/ssltest/`

---

## Testing Checklist

### Before DNS Migration

- [ ] All pages load correctly on GitHub Pages URL
- [ ] All blog posts accessible
- [ ] Newsletter archive works
- [ ] Downloads work
- [ ] Images load correctly
- [ ] Navigation works
- [ ] Links are correct
- [ ] Mobile responsive
- [ ] No broken links

### After DNS Migration

- [ ] Site loads at handyworks.com
- [ ] SSL certificate active (HTTPS)
- [ ] All pages accessible
- [ ] Old WordPress site no longer accessible (or redirects)
- [ ] Search engines can index new site
- [ ] Monitor for 404 errors

---

## Rollback Plan

If issues occur after DNS migration:

1. **Quick Rollback:**
   - Revert DNS CNAME/A records to WordPress server
   - Wait for DNS propagation
   - Site returns to WordPress

2. **Keep GitHub Pages:**
   - Fix issues on GitHub Pages
   - Test on GitHub Pages URL
   - Re-migrate DNS when ready

---

## Post-Migration Tasks

1. **Update Search Engines:**
   - Submit new sitemap to Google Search Console
   - Update Bing Webmaster Tools
   - Monitor indexing

2. **Set Up Redirects (if needed):**
   - Old WordPress URLs → New static URLs
   - Can be done via `.htaccess` on old server or GitHub Pages redirects

3. **Monitor:**
   - Check analytics
   - Monitor 404 errors
   - Verify all functionality

---

## Current Status

✅ **Repository:** Ready  
✅ **GitHub Pages:** Ready to configure  
⏳ **Testing:** Pending  
⏳ **DNS Migration:** Pending  

---

## Notes

- **Old Site:** WordPress remains live at handyworks.com during testing
- **Test URL:** `https://sbschram.github.io/handyworks-website/`
- **No Downtime:** DNS migration can be done with minimal downtime
- **SSL:** Automatic via GitHub Pages (Let's Encrypt)

---

**Next Step:** Commit and push changes, then configure GitHub Pages

