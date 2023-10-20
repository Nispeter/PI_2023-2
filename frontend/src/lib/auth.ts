import { createAuth0Client } from '@auth0/auth0-spa-js';
import { ENV } from './env';
import { authClient, isAuthenticated, popUpOpen, user } from '../store';
import { get } from 'svelte/store';

async function createClient() {
	authClient.set(
		await createAuth0Client({
			domain: ENV.auth0.domain,
			clientId: ENV.auth0.id,
			authorizationParams: {
				redirect_uri: ENV.auth0.callback,
				scope: 'openid profile email'
			}
		})
	);
}

async function loginWithPopup() {
	popUpOpen.set(true);
	try {
		const client = get(authClient);
		await client.loginWithPopup();
		const userData = await client.getUser();
		user.set(userData ?? {});
		isAuthenticated.set(await client.isAuthenticated());
	} catch (e) {
		console.error(e);
	} finally {
		popUpOpen.set(false);
	}
}

async function login() {
	try {
		get(authClient).loginWithRedirect();
		// console.log("is Authenticated value", get(isAuthenticated));
		// user.set((await client.getUser()) ?? {});
		// isAuthenticated.set(true);
		// console.log(get(user), get(isAuthenticated));
	} catch (e) {
		console.error(e);
	}
}

async function logout() {
	try {
		await get(authClient).logout({
			logoutParams: {
				returnTo: 'http://localhost:5173/login'
			}
		});
	} catch (e) {
		console.error(e);
	}
}

export const auth = {
	createClient,
	login,
	loginWithPopup,
	logout
};
