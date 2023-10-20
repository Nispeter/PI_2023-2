<script lang="ts">
	import { auth } from '$lib/auth';
	import { Table } from '@skeletonlabs/skeleton';
	import type { TableSource } from '@skeletonlabs/skeleton';
	import { tableMapperValues } from '@skeletonlabs/skeleton';
	import { AppBar } from '@skeletonlabs/skeleton';
	import { onMount } from 'svelte';


	onMount(async ()=> {
		await auth.createClient();
	})

	async function logout() {
		await auth.logout();
	}
	const sourceData = [
		{ nombreDueño: 'Luis Bello', nPatente: 'RH ZX 64', Hora: '20:15', Fecha: '05/10/2023' },
		{ nombreDueño: 'Maria Espinoza', nPatente: 'MR LX 88', Hora: '20:07', Fecha: '05/10/2023' },
		{ nombreDueño: 'Francisca Fuentes', nPatente: 'WC BM 72', Hora: '19:48', Fecha: '05/10/2023' },
		{ nombreDueño: 'Fernando Reyes', nPatente: 'LD MN 96', Hora: '19:32', Fecha: '05/10/2023' },
		{ nombreDueño: 'José Zapata', nPatente: 'FN KK 56', Hora: '15:22', Fecha: '05/10/2023' },
		{ nombreDueño: 'Marco Aguirre', nPatente: 'MH GH 80', Hora: '15:03', Fecha: '05/10/2023' },
		{ nombreDueño: 'Luis Bello', nPatente: 'RH ZX 64', Hora: '08:15', Fecha: '05/10/2023' },
		{ nombreDueño: 'Isabel Gonzales', nPatente: 'KV BM 77', Hora: '08:11', Fecha: '05/10/2023' },
		{ nombreDueño: 'Paola Rojas', nPatente: 'KL FM 59', Hora: '22:50', Fecha: '04/10/2023' },
		{ nombreDueño: 'Maria Ignacia Rosas', nPatente: 'HN MN 61', Hora: '20:30', Fecha: '04/10/2023' }
	];

	const tableSimple: TableSource = {
		head: ['Nombre', 'Número Patente', 'Hora', 'Fecha'],
		body: tableMapperValues(sourceData, ['nombreDueño', 'nPatente', 'Hora', 'Fecha']),
		meta: tableMapperValues(sourceData, ['nombreDueño', 'nPatente', 'Hora', 'Fecha'])
	};
</script>

<AppBar slotTrail="place-content-end">
	<h1 class="h1 font-sans" data-toc-ignore>Historial de avistamiento de vehiculos</h1>
	<h3 class="h3 font-sans" data-toc-ignore>
		Bienvenidos a su aplicacion de reconocimiento de vehiculos
	</h3>

	<svelte:fragment slot="trail">
		<button type="button" class="btn variant-filled-primary" on:click={logout}>Logout</button>
	</svelte:fragment>
</AppBar>

<div class="w-full p-10">
	<div class="flex justify-end">
		<div>
			<button type="button" class="btn variant-filled">Administrar Base de Datos</button>
		</div>
	</div>
</div>
<div class="px-20 py-5">
	<Table source={tableSimple} />
</div>
