# Step-by-Step Server cPanel Guide

**Current Location:** Server cPanel Login Page  
**Goal:** Access WordPress installation and begin content recovery

---

## Step 1: Log into Server cPanel

### At the Login Page:
1. **Select Language:** Choose "English" (or your preferred language)
2. **Enter Username:** Your cPanel username
3. **Enter Password:** Your cPanel password
4. **Click "Log in"**

**Note:** If you don't remember your credentials, click "Reset Password"

---

## Step 2: Find WordPress Installation

Once logged into cPanel, you'll see the main dashboard. WordPress could be in several places:

### Option A: Softaculous Apps Installer (Most Common)
1. Look for **"Softaculous Apps Installer"** icon in cPanel
2. Click on it
3. Look for **"WordPress"** in the list of applications
4. Click on **"WordPress"**
5. You'll see your WordPress installation(s)
6. Click **"Installations"** tab to see all WordPress sites

### Option B: WordPress Manager (if installed)
1. Look for **"WordPress"** or **"WordPress Manager"** icon
2. Click on it
3. This will show all WordPress installations on the server

### Option C: File Manager (Manual Method)
1. Click **"File Manager"** icon
2. Navigate to your domain's root directory:
   - Usually `public_html/` for main domain
   - Or `public_html/subdomain/` for subdomain
3. Look for WordPress files:
   - `wp-config.php` (confirms WordPress is there)
   - `wp-admin/` folder
   - `wp-content/` folder

---

## Step 3: Access WordPress Admin

### If Using Softaculous:
1. Find your WordPress installation in the list
2. Click the **"Admin"** button (or pencil icon to edit)
3. This will take you to WordPress admin login
4. **OR** click **"Login"** button which opens WordPress admin

### If Using File Manager:
1. Navigate to your WordPress root directory
2. The admin URL is usually:
   - `https://www.handyworks.com/wp-admin/`
   - Or `https://www.handyworks.com/wp-login.php`

### Direct WordPress Admin Access:
Try these URLs in a new browser tab:
- `https://www.handyworks.com/wp-admin/`
- `https://www.handyworks.com/wp-login.php`

**WordPress Login Credentials:**
- These are **different** from cPanel credentials
- Username: (may be different from cPanel username)
- Password: (WordPress password, not cPanel password)

**If you don't remember WordPress credentials:**
- You can reset via Softaculous (if available)
- Or reset via File Manager (edit `wp-config.php` or use WordPress password reset)

---

## Step 4: Export WordPress Content (Once in WordPress Admin)

### A. Export All Content
1. In WordPress admin, go to **Tools** → **Export** (left sidebar)
2. Select **"All content"**
3. Click **"Download Export File"**
4. Save the file (XML format)
5. **Compare with existing:** `handyworks.WordPress.2025-10-29.xml`

### B. Check Content Counts
1. **Posts:** Go to **Posts** → **All Posts** (note total count)
2. **Pages:** Go to **Pages** → **All Pages** (note total count)
3. **Media:** Go to **Media** → **Library** (note total count)

---

## Step 5: Access Database (phpMyAdmin)

### From cPanel Dashboard:
1. Look for **"phpMyAdmin"** icon in cPanel
2. Click on it
3. In the left sidebar, you'll see databases
4. Look for database with WordPress name (usually contains `wp` or `wordpress` or `handyworks`)
5. Click on the database name

### Find WordPress Database:
- Database name might be: `handyworks_wp`, `handyworks_wordpress`, `username_wp`, etc.
- Look for database with many tables (WordPress has ~12 default tables)
- Tables usually start with `wp_` prefix (or custom prefix)

### Export Database:
1. Click **"Export"** tab (top menu)
2. Select **"Quick"** export method
3. Format: **SQL**
4. Click **"Go"** button
5. Save the file: `handyworks-wordpress-database-YYYY-MM-DD.sql`

---

## Step 6: Download Media Files

### Using File Manager:
1. Go back to cPanel dashboard
2. Click **"File Manager"**
3. Navigate to your WordPress installation directory
4. Go to: `wp-content/uploads/`
5. Select the entire `uploads` folder
6. Click **"Compress"** (top menu)
7. Choose **ZIP** format
8. Click **"Compress File(s)"**
9. Wait for compression to complete
10. Right-click the ZIP file
11. Click **"Download"**
12. Save to your local computer

**Note:** This may be a large file. Be patient during compression and download.

---

## Step 7: Quick Content Check (Without WordPress Admin)

### If you can't access WordPress admin, you can still check:

#### Via File Manager:
1. Navigate to WordPress root directory
2. Check `wp-content/uploads/` for media files
3. Count files/folders to estimate media library size

#### Via phpMyAdmin:
1. Access phpMyAdmin from cPanel
2. Select WordPress database
3. Click on `wp_posts` table (or `yourprefix_posts`)
4. Check row count:
   - Filter by `post_type = 'post'` for blog posts
   - Filter by `post_type = 'page'` for pages
   - Filter by `post_type = 'attachment'` for media

---

## Simplified Recovery Plan

### Since you already have the XML export:

**What the XML contains:**
- ✅ All blog posts (61 posts found)
- ✅ All pages (15 pages found)
- ✅ Media references (42 attachments found)
- ✅ Categories and tags
- ✅ Post dates and metadata

**What you still need:**
- ⚠️ **Actual media files** (images, PDFs) - download from `/wp-content/uploads/`
- ⚠️ **Fresh export** (if any new content since Oct 29, 2025)

**Minimal cPanel tasks:**
1. **Download media files** (File Manager → wp-content/uploads → compress & download)
2. **Optional:** Fresh WordPress export (if you can access WordPress admin)
3. **Optional:** Database export (for custom fields/plugin data)

---

## Quick Checklist

After accessing cPanel, you should:

- [ ] Locate WordPress installation (Softaculous or File Manager)
- [ ] Access WordPress admin (if possible)
- [ ] Download media files from `/wp-content/uploads/`
- [ ] Optional: Export fresh WordPress content
- [ ] Optional: Export database via phpMyAdmin

---

## Troubleshooting

### Can't find WordPress:
- Check if it's in a subdirectory (like `/blog` or `/wp`)
- Look in File Manager for `wp-config.php` file
- Check Softaculous Apps Installer
- WordPress might be installed in a subdomain

### Can't access WordPress admin:
- Try direct URL: `https://www.handyworks.com/wp-admin/`
- Check if WordPress is in subdirectory: `https://www.handyworks.com/blog/wp-admin/`
- Reset password via Softaculous (if available)
- Check File Manager for `wp-config.php` to find database details

### Media files too large:
- Download in batches (by year folders: 2024/, 2023/, etc.)
- Use FTP instead of File Manager (if available in cPanel)
- Compress individual year folders separately

### Database not found:
- Check `wp-config.php` in File Manager for database name
- Look for database with many tables (WordPress has ~12+ tables)
- Database name might have a prefix like `username_` or `handyworks_`

---

## Most Important Task

**Since you already have the XML export with all content:**

**Priority 1:** Download media files
- File Manager → wp-content/uploads → Compress → Download

**Priority 2:** Check if you need fresh export
- Access WordPress admin → Tools → Export
- Compare dates with existing export (Oct 29, 2025)

**Priority 3:** Database export (optional)
- phpMyAdmin → Select database → Export → SQL

---

**Status:** Ready to access cPanel and download media files
