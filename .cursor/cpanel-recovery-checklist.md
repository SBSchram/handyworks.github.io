# cPanel Recovery Checklist

**Purpose:** Systematic recovery of all WordPress content and configuration using cPanel access.

---

## Step 1: WordPress Admin Access

### Access WordPress Dashboard
- [ ] Log into cPanel
- [ ] Locate WordPress installation
- [ ] Access WordPress admin dashboard
- [ ] Document WordPress version
- [ ] Document active theme
- [ ] List all active plugins

### Document Current Setup
- [ ] Take screenshots of WordPress admin
- [ ] Document customizations
- [ ] Note any custom post types
- [ ] Document widget configurations
- [ ] Note menu structure

---

## Step 2: Database Export

### Via cPanel phpMyAdmin
- [ ] Access phpMyAdmin from cPanel
- [ ] Select WordPress database
- [ ] Export complete database (SQL format)
- [ ] Save as: `handyworks-wordpress-database-YYYY-MM-DD.sql`
- [ ] Verify export file size (should be substantial)

### Database Content Inventory
- [ ] Count total posts
- [ ] Count total pages
- [ ] Count total media items
- [ ] List all custom post types
- [ ] Document custom fields
- [ ] Note any custom tables

---

## Step 3: Media Library Recovery

### Download Media Files
- [ ] Access File Manager in cPanel
- [ ] Navigate to `/wp-content/uploads/`
- [ ] Download entire uploads directory
- [ ] Organize by year/month structure
- [ ] Verify all images downloaded
- [ ] Check for PDFs and documents

### Media Inventory
- [ ] Create list of all media files
- [ ] Document file sizes
- [ ] Note any missing files
- [ ] Check for external media links

---

## Step 4: Content Export

### WordPress Export Tool
- [ ] Use WordPress Tools > Export
- [ ] Export "All content"
- [ ] Save as: `handyworks-wordpress-export-YYYY-MM-DD.xml`
- [ ] Compare with existing export (2025-10-29.xml)
- [ ] Note any differences

### Content Types to Export
- [ ] Posts (all)
- [ ] Pages (all)
- [ ] Media (references)
- [ ] Comments (if any)
- [ ] Custom post types
- [ ] Categories and tags

---

## Step 5: Configuration Recovery

### WordPress Settings
- [ ] General settings (site title, tagline, URLs)
- [ ] Reading settings (homepage, blog page)
- [ ] Permalink structure
- [ ] Discussion settings
- [ ] Privacy settings

### Plugin Configurations
- [ ] List all plugins and their settings
- [ ] Document plugin purposes
- [ ] Note any custom plugin data
- [ ] Export plugin configurations (if possible)

### Theme Customizations
- [ ] Document theme customizations
- [ ] Export custom CSS
- [ ] Note widget areas
- [ ] Document menu locations

---

## Step 6: Domain & DNS Information

### Current DNS Settings
- [ ] Document current DNS records (from cPanel)
- [ ] Note A records
- [ ] Note CNAME records
- [ ] Note MX records (email)
- [ ] Document nameservers

### Domain Information
- [ ] Domain registrar
- [ ] Domain expiration date
- [ ] DNS management location
- [ ] SSL certificate details
- [ ] Email hosting (if separate)

---

## Step 7: SEO & Analytics

### SEO Data
- [ ] Export meta descriptions (if using SEO plugin)
- [ ] Export meta titles
- [ ] Document focus keywords
- [ ] Export sitemap (if exists)
- [ ] Note canonical URLs

### Analytics
- [ ] Google Analytics ID (if applicable)
- [ ] Other tracking codes
- [ ] Document analytics setup

---

## Step 8: Email Configuration

### Email Settings
- [ ] Email accounts in cPanel
- [ ] Forwarding rules
- [ ] Auto-responders
- [ ] Email routing

### Contact Forms
- [ ] Document contact form setup
- [ ] Export form submissions (if any)
- [ ] Note form fields
- [ ] Document email recipients

---

## Step 9: Security & Access

### User Accounts
- [ ] List all WordPress users
- [ ] Document user roles
- [ ] Note admin accounts
- [ ] Export user data (if needed)

### Security Settings
- [ ] Document security plugins
- [ ] Note firewall rules
- [ ] Document access restrictions
- [ ] Note IP whitelists/blacklists

---

## Step 10: Backup & Archive

### Complete Backup
- [ ] Full cPanel backup (if available)
- [ ] WordPress files backup
- [ ] Database backup
- [ ] Media library backup
- [ ] Configuration backup

### Archive Organization
- [ ] Create backup directory structure
- [ ] Organize all exports
- [ ] Document backup locations
- [ ] Verify backup integrity

---

## Content Recovery Priority

### High Priority (Immediate)
1. Database export
2. Media library download
3. WordPress export (all content)
4. Current pages/posts inventory

### Medium Priority (Week 1)
5. Plugin configurations
6. Theme customizations
7. SEO data
8. Newsletter content

### Low Priority (As Needed)
9. User accounts
10. Security settings
11. Email configurations
12. Analytics setup

---

## Recovery Tools Needed

### From cPanel
- File Manager
- phpMyAdmin
- WordPress admin
- Backup tools

### Local Tools
- XML parser (for WordPress export)
- SQL viewer (for database)
- File organizer
- Content extraction scripts

---

## Notes

- **WordPress Export XML:** Already have `handyworks.WordPress.2025-10-29.xml` (7,440 lines)
- **Compare:** New export vs existing export to identify any new content
- **Media:** May need to download large files in batches
- **Database:** Full SQL export provides complete data recovery
- **Timing:** Do this before making any changes to WordPress site

---

## Questions to Answer

1. How many total blog posts are in WordPress?
2. Are all newsletters in WordPress or elsewhere?
3. Is Reports List page in WordPress?
4. Are there any custom post types?
5. What plugins are critical to preserve functionality?
6. Is there e-commerce functionality?
7. Are there any custom database tables?

---

**Status:** Ready to begin recovery process

