import type { Auth0Client } from '@auth0/auth0-spa-js';
import { writable, type Writable } from 'svelte/store';

export const isAuthenticated = writable(false);
export const user = writable({});
export const popUpOpen = writable(false);
export const error = writable();
export const authClient: Writable<Auth0Client> = writable();
