/**
 * Well Circle — API client for frontend.
 * All backend calls go through this module.
 */

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

let authToken = null;

export function setAuthToken(token) {
  authToken = token;
  localStorage.setItem('wc_token', token);
}

export function getAuthToken() {
  if (!authToken) {
    authToken = localStorage.getItem('wc_token');
  }
  return authToken;
}

export function clearAuth() {
  authToken = null;
  localStorage.removeItem('wc_token');
}

async function request(method, path, body = null) {
  const headers = { 'Content-Type': 'application/json' };
  const token = getAuthToken();
  if (token) headers['Authorization'] = `Bearer ${token}`;

  const opts = { method, headers };
  if (body) opts.body = JSON.stringify(body);

  const res = await fetch(`${API_BASE}${path}`, opts);

  if (res.status === 401) {
    clearAuth();
    window.location.reload();
    throw new Error('Unauthorized');
  }

  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Request failed' }));
    throw new Error(err.detail || JSON.stringify(err));
  }

  return res.json();
}

// --- Auth ---
export const auth = {
  telegram: (initData) => request('POST', '/auth/telegram', { init_data: initData }),
};

// --- Users ---
export const users = {
  me: () => request('GET', '/users/me'),
  onboard: (data) => request('POST', '/users/me/onboard', data),
  update: (data) => request('PATCH', '/users/me', data),
  pointsHistory: () => request('GET', '/users/me/points-history'),
};

// --- Providers ---
export const providers = {
  list: (params = {}) => {
    const qs = new URLSearchParams(params).toString();
    return request('GET', `/providers${qs ? '?' + qs : ''}`);
  },
  detail: (id) => request('GET', `/providers/${id}`),
  stats: (id) => request('GET', `/providers/${id}/stats`),
};

// --- Communities ---
export const communities = {
  list: (params = {}) => {
    const qs = new URLSearchParams(params).toString();
    return request('GET', `/communities${qs ? '?' + qs : ''}`);
  },
  detail: (id) => request('GET', `/communities/${id}`),
  join: (id) => request('POST', `/communities/${id}/join`),
  leave: (id) => request('POST', `/communities/${id}/leave`),
  checkin: (id) => request('POST', `/communities/${id}/checkin`),
  feed: (id, since = null, limit = 20) => {
    const params = new URLSearchParams({ limit });
    if (since) params.set('since', since);
    return request('GET', `/communities/${id}/feed?${params}`);
  },
};

// --- Bookings ---
export const bookings = {
  create: (data) => request('POST', '/bookings', data),
};

// --- Payments ---
export const payments = {
  telebirrInitiate: (bookingId) => request('POST', '/payments/telebirr/initiate', { booking_id: bookingId }),
  mpesaInitiate: (bookingId, phone) => request('POST', '/payments/mpesa/initiate', { booking_id: bookingId, phone_number: phone }),
  status: (bookingId) => request('GET', `/payments/${bookingId}/status`),
};

// --- Admin ---
export const admin = {
  analytics: () => request('GET', '/admin/analytics'),
  users: (params = {}) => {
    const qs = new URLSearchParams(params).toString();
    return request('GET', `/admin/users${qs ? '?' + qs : ''}`);
  },
  userByTelegram: (tgId) => request('GET', `/admin/users/${tgId}`),
  createProvider: (data) => request('POST', '/admin/providers', data),
  updateProvider: (id, data) => request('PUT', `/admin/providers/${id}`, data),
  deleteProvider: (id) => request('DELETE', `/admin/providers/${id}`),
};
