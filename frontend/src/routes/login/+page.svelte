<script lang="ts">
	import { auth } from '$lib/auth';
	import { onMount } from 'svelte';
	import { isAuthenticated, user, authClient } from '../../store';
	import { goto } from '$app/navigation';
	import { get } from 'svelte/store';

	onMount(async () => {
		await auth.createClient();

		await auth.loginWithPopup();


		if (get(isAuthenticated)) {
			return goto('/historial');
		}

	});

	async function login() {
	}

	function logout() {
		auth.logout();
	}
</script>

<svelte:head>
	<title>
		Login
	</title>
</svelte:head>
<!-- <section>
	<div class="flex h-screen items-center">
		<div class="card w-1/2 mx-auto h-1/2">
			<header class="card-header text-center text-4xl">Inicio de Sesion</header>
			<div class="grid grid-cols-1 justify-items-center h-full place-content-center">
				<button class="btn rounded-md variant-filled-primary" on:click={login}
					>Iniciar Sesion</button
				>
				<button class="btn rounded-md variant-filled-primary" on:click={logout}>Logout</button>
			</div>
		</div>
	</div>
</section> -->
