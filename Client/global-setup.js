import { chromium } from '@playwright/test';

async function globalSetup() {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  const port = process.env.PLAYWRIGHT_PORT || process.env.PORT || 5176;
  const base = process.env.PLAYWRIGHT_BASE_URL || `http://localhost:${port}`;

  await page.goto(`${base}/login`);

  // Wait for the form to appear
  await page.waitForSelector('form', { timeout: 10000 });

  // Username is first input, password is second (type=password)
  await page.locator('input.form-control').first().fill('testuser');
  await page.locator('input[type="password"]').fill('Test@1234');

  await page.locator('button[type="submit"]').click();

  // Wait for redirect to home
  await page.waitForURL(url => !url.toString().includes('/login'), { timeout: 10000 });

  // Seed a test book list in localStorage so tests that run without a
  // fully-seeded backend can still validate UI flows.
  const seed = [{ id: 'seed-1', publisher: 'SeedPub', name: 'Seed Book', date: '2025-01-01', cost: 10.0 }];
  await page.evaluate((books) => {
    try { localStorage.setItem('test_books', JSON.stringify(books)); } catch (e) {}
  }, seed);

  // Save auth state (includes localStorage seeded above) so test contexts
  // reuse both auth and the seeded books.
  await page.context().storageState({ path: 'auth-state.json' });

  await browser.close();
}

export default globalSetup;
