import { defineConfig, devices } from '@playwright/test';

// Allow overriding the dev server port/url via env vars when running tests.
const port = process.env.PLAYWRIGHT_PORT || process.env.PORT || 5176;
const base = process.env.PLAYWRIGHT_BASE_URL || `http://localhost:${port}`;

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  timeout: 60000,

  globalSetup: './global-setup.js',

  use: {
    baseURL: base,
    storageState: 'auth-state.json',  // reuse login for every test
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    actionTimeout: 10000,
    navigationTimeout: 30000,
  },

  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],

  webServer: {
    // Start vite on the requested port so Playwright can manage lifecycle,
    // but reuse existing server if already running.
    command: `npm run dev -- --port ${port}`,
    url: base,
    reuseExistingServer: true,
    timeout: 180000,
    stdout: 'pipe',
    stderr: 'pipe',
  },
});
