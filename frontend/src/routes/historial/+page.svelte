<script lang="ts">
	import { auth } from '$lib/auth';
	import { Table } from '@skeletonlabs/skeleton';
	import { tableMapperValues } from '@skeletonlabs/skeleton';
	import { AppBar } from '@skeletonlabs/skeleton';
	import { Paginator } from '@skeletonlabs/skeleton';
	import type { PaginationSettings } from '@skeletonlabs/skeleton';
	import { onMount } from 'svelte';
	import { get } from 'svelte/store';
	import { isAuthenticated } from '../../store';
	import { goto } from '$app/navigation';
	import logoutIcon from '$lib/images/logout.svg';
	import type { DataH } from './type';
	import AxiosSugar from 'axios-sugar';

	// Se define hi como un datatype DataH o como null
	let hi: DataH[] | null = [];

	onMount(async () => {
		// Login
		if (!get(isAuthenticated)) {
			goto('/login');
		}

		// Request cada 10 segundos
		let myInterval = setInterval(async () => {
			try {
				// Request al Endpoint
				const result = await AxiosSugar.get(
					'http://localhost:8000/horarios',
					{},
					{
						// intervalo de tiempo para hacer las requests
						repeat: {
							interval: 1000
						}
					}
				);
				// Se guarda los datos en hi
				hi = result.data;
				// Para casos no nulos se parsea la fecha a un dato mas amigable
				hi?.forEach((values) => {
					const date = new Date(values.time);
					values.time = date.toLocaleString();
				});
			// Se recoge el error en caso de haberlo y se envia un mensaje
			} catch (error) {
				console.error(error);
			}
		}, 5000);
	});

	// Funcion de log out
	async function logout() {
		await auth.logout();
	}

	// Parametros para la paginacion
	let paginationSettings = {
		page: 0,
		limit: 10,
		size: hi!.length,
		amounts: [1, 2, 5, 10]
	} satisfies PaginationSettings;

	// Aqui se hace un slice de los datos para poder hacer una paginacion de tabla
	$: paginatedSource = hi!.slice(
		paginationSettings.page * paginationSettings.limit,
		paginationSettings.page * paginationSettings.limit + paginationSettings.limit
	);

	// Funcion para hacer que al precionar un boton vaya a la pagina de patentes
	const goPatentes = () => {
		goto('/patentes');
	};
</script>

<svelte:head>
	<title>Historial</title>
</svelte:head>

<AppBar slotTrail="place-content-end">
	<h1 class="h1" data-toc-ignore>Historial de avistamiento de vehiculos</h1>
	<h3 class="h3" data-toc-ignore>Bienvenidos a su aplicacion de reconocimiento de vehiculos</h3>

	<svelte:fragment slot="trail">
		<!-- Boton para hacer log out -->
		<button type="button" class="btn variant-filled-primary" on:click={logout}>
			<span class="text-white">Cerrar Sesion</span>
			<picture>
				<img src={logoutIcon} alt="salir" width="20" height="20" />
			</picture>
		</button>
	</svelte:fragment>
</AppBar>

<div class="w-full p-10">
	<div class="flex justify-end">
		<div>
			<!-- Boton para ir a la pagina de administracion -->
			<button type="button" class="btn variant-filled" on:click={goPatentes}
				>Administrar Residente</button
			>
		</div>
	</div>
</div>
<div class="px-20 py-5">
	<!-- Tabla con paginacion -->
	<Table
		source={{
			head: ['Número Patente', 'Fecha', 'Camara'],
			body: tableMapperValues(paginatedSource, ['licence', 'time', 'lugar'])
		}}
		interactive={true}
	/>
	<Paginator
		bind:settings={paginationSettings}
		showFirstLastButtons={true}
		showPreviousNextButtons={true}
	/>
</div>