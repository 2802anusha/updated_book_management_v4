import { chromium } from '@playwright/test';

async function globalSetup() {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // 1. Ensure backend is reachable (health check)
  const backendUrl = 'http://localhost:5001';
  try {
    const health = await page.request.get(`${backendUrl}/health`);
    if (!health.ok()) throw new Error(`Backend health check failed: ${health.status()}`);
    console.log('✅ Backend is healthy');
  } catch (err) {
    console.error('❌ Backend not reachable:', err);
    throw err;
  }

  // 2. Login via API and store token directly
  const loginRes = await page.request.post(`${backendUrl}/login`, {
    data: { username: 'testuser', password: 'Test@1234' }
  });
  if (!loginRes.ok()) {
    throw new Error(`Login failed: ${loginRes.status()} ${await loginRes.text()}`);
  }
  const { access_token } = await loginRes.json();

  // 3. Save token to localStorage (so it's available for all tests)
  await page.addInitScript((token) => {
    window.localStorage.setItem('access_token', token);
  }, access_token);

  // 4. Save storage state for reuse
  await page.context().storageState({ path: 'auth-state.json' });

  await browser.close();
  console.log('✅ Global setup complete – token saved');
}

export default globalSetup;