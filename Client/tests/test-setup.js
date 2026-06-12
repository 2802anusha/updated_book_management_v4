import { test as baseTest } from '@playwright/test';

// Global setup with page fixture
export const test = baseTest.extend({
  page: async ({ browser }, use) => {
    const context = await browser.newContext({
      viewport: { width: 1280, height: 720 }
    });
    // Ensure tests run with a logged-in state so routes requiring auth are reachable
    await context.addInitScript(() => {
      try {
        localStorage.setItem('access_token', 'test-token');
      } catch (e) {}
    });
    const page = await context.newPage();

    // Navigate to the app before each test. Use PLAYWRIGHT_BASE_URL if provided
    // (set by the runner) or fall back to a likely Vite port.
    const baseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://localhost:5176';
    await page.goto(baseUrl);
    
    await use(page);
    
    await context.close();
  },
});

export const expect = test.expect;