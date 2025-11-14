# Contact Form Security

## Current Setup

The contact form uses **Formspree** (https://formspree.io), which provides:

✅ **Built-in Spam Protection:**
- Automatic spam filtering
- Honeypot fields
- Rate limiting
- IP-based blocking
- Machine learning spam detection

## Do You Need reCAPTCHA?

**Short Answer: Probably not.** Formspree's built-in protection is usually sufficient for most sites.

### When to Add reCAPTCHA:

- If you're receiving a lot of spam despite Formspree's protection
- If you want an extra visible layer of security
- If you have compliance requirements that mandate it

### How to Add reCAPTCHA (if needed):

1. **Get reCAPTCHA Keys:**
   - Go to https://www.google.com/recaptcha/admin
   - Register your site
   - Get Site Key and Secret Key

2. **Add to contact.html:**
   ```html
   <!-- Add before closing </head> -->
   <script src="https://www.google.com/recaptcha/api.js" async defer></script>
   
   <!-- Add before submit button -->
   <div class="g-recaptcha" data-sitekey="YOUR_SITE_KEY"></div>
   ```

3. **Configure Formspree:**
   - In Formspree dashboard, enable reCAPTCHA verification
   - Add your Secret Key

## Recommendation

**Start without reCAPTCHA** - Formspree's protection is usually enough. Only add it if you start receiving spam.

## Cloudflare

Cloudflare is a CDN/security service that can:
- Speed up your site (though GitHub Pages already uses a CDN)
- Add DDoS protection
- Add additional security layers

**For a static GitHub Pages site, Cloudflare is optional** - GitHub Pages already provides:
- Fast global CDN
- DDoS protection
- SSL certificates

You might consider Cloudflare if:
- You want more control over caching
- You need advanced security features
- You want analytics
- You're planning to use a custom domain with advanced DNS features

