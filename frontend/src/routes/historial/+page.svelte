<script lang="ts">
	import { auth } from '$lib/auth';
	import { Table } from '@skeletonlabs/skeleton';
	import type { PageData } from './$types';
	import type { TableSource } from '@skeletonlabs/skeleton';
	import { tableMapperValues } from '@skeletonlabs/skeleton';
	import { tableSourceMapper } from '@skeletonlabs/skeleton';
	import { AppBar } from '@skeletonlabs/skeleton';
	import { Paginator } from '@skeletonlabs/skeleton';
	import type { PaginationSettings } from '@skeletonlabs/skeleton';
	import { onMount } from 'svelte';
	import { get } from 'svelte/store';
	import { isAuthenticated } from '../../store';
	import { goto } from '$app/navigation';
	import logoutIcon from '$lib/images/logout.svg';
	import type { DataH, Dueño, Propietario, Lugar } from './type';
	import axios from 'axios';
	import AxiosSugar from 'axios-sugar';

	// Se define el tipo de dato para hi
	let hi: DataH[] | null = [];

	// Se llama el intervalo de soporte para las requests
	AxiosSugar.defaults = {
		repeat: {
			interval: 5000 //5s
		}
	}

	onMount(async () => {
		// Autentificacion por login
		if (!get(isAuthenticated)) {
			goto('/login');
		}
		// Funcion de Axios que en intervalos de 5 segundos hace la request de get para los datos del URL 
		let myInterval = setInterval(async () => {
			try {
				// Get mediante axiosSugar para manejar las request repetitivas
				const result = await AxiosSugar.get('http://localhost:8000/horarios');
				//console.log(result);
				hi = result.data;
				//console.log(hi); para verificar el intervalo
			} catch (error) {
				console.error(error);
				hi = [];
			}		
		}, 5000); 
	});

	async function logout() {
		await auth.logout();
	}

	/* async function doGetRequest() {

		const params = hi;

		const d: Dueño[] = await axios.get(`http://localhost:8000/autos/patentes?${params}`).then(
			(res) => res.data
		)
		return {
			d
		};
	} */

	// Configuracion de la paginacion
	let paginationSettings = {
		page: 0,
		limit: 10,
		size: hi!.length,
		amounts: [1, 2, 5, 10]
	} satisfies PaginationSettings;

	// Se obtiene el Source de la paginacion mediante el slice de hi, que contiene los datos del request
	$: paginatedSource = hi!.slice(
		paginationSettings.page * paginationSettings.limit,
		paginationSettings.page * paginationSettings.limit + paginationSettings.limit
	);

	// Funcion para el boton
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
		<button type="button" class="btn-icon variant-filled-primary" on:click={logout}>
			<picture>
				<img src={logoutIcon} alt="salir" width="20" height="20" />
			</picture>
		</button>
	</svelte:fragment>
</AppBar>

<div class="w-full p-10">
	<div class="flex justify-end">
		<div>
			<!-- Boton que llega al servicio de administracion de datos -->
			<button type="button" class="btn variant-filled" on:click={goPatentes}
				>Administrar Base de Datos</button
			>
		</div>
	</div>
</div>
<div class="px-20 py-5">
	<!-- Tabla que obtiene sus datos de pagginatesSource-->
	<Table
		source={{
			head: ['Número Patente', 'Fecha'],
			body: tableMapperValues(paginatedSource, ['licence', 'time'])
		}}
		interactive={true}
	/>
	<!-- Paginador que permite que la tabla tenga distintas paginas para mejor visualizacion de los datos -->
	<Paginator
		bind:settings={paginationSettings}
		showFirstLastButtons={true}
		showPreviousNextButtons={true}
	/>
</div>
