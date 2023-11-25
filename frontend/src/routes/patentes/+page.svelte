<script lang="ts">
	import { auth } from '$lib/auth';
	import type { PageData } from './$types';
	import { Table, tableMapperValues } from '@skeletonlabs/skeleton';
	import type { PaginationSettings, TableSource } from '@skeletonlabs/skeleton';
	import { Paginator, AppBar } from '@skeletonlabs/skeleton';
	import { onMount, type ComponentEvents } from 'svelte';
	import { isAuthenticated } from '../../store';
	import { goto } from '$app/navigation';
	import { get } from 'svelte/store';
	import backArrow from '$lib/images/back-arrow.svg';
	import logoutIcon from '$lib/images/logout.svg';
	import plusIcon from '$lib/images/plus.svg';
	import { Modal, getModalStore, initializeStores } from '@skeletonlabs/skeleton';
	import type { ModalSettings, ModalComponent } from '@skeletonlabs/skeleton';
	import modalForm from './modalForm.svelte';
	import axios from 'axios';

	initializeStores();

	export let data: PageData;

	const modalStore = getModalStore();

	const modalRegistry: Record<string, ModalComponent> = {
		modalComponent: { ref: modalForm }
	};

	// modalStore.trigger(modal);
	if ($modalStore[0]) console.log($modalStore[0].title);

	onMount(async () => {
		if (!get(isAuthenticated)) {
			goto('/login');
		}
	});

	async function logout() {
		await auth.logout();
	}
	let paginationSettings = {
		page: 0,
		limit: 5,
		size: data.allCars.length,
		amounts: [1, 2, 5, 10]
	} satisfies PaginationSettings;

	$: paginatedSource = data.allCars!.slice(
		paginationSettings.page * paginationSettings.limit,
		paginationSettings.page * paginationSettings.limit + paginationSettings.limit
	);
	let modalFlag: boolean = false;
	function triggerModal() {
		new Promise<boolean>((resolve) => {
			const modal: ModalSettings = {
				title: 'Ingresar registro.',
				body: 'Rellene el formulario.',
				type: 'component',
				component: 'modalComponent',
				response: (r: boolean) => {
					/**
					puedes definir aqui el post pero esta debe ser una funcion asyncrona  
					de definir el post dentro de modalForm entonces debes seguir esto
					https://www.skeleton.dev/utilities/modals#async-response
					**/
					resolve(r);
				}
			};
			modalStore.trigger(modal);
			modalFlag = true;
		}).then(async (r: any) => {
			//PReguntar por error => triggerear modal.
			if (r.response == false) {
				const modal: ModalSettings = {
					type: 'alert',
					// Data
					title: 'Error al registrar.',
					body: 'Algo ha salido mal. Verifique los campos, si este error persiste contactar con soporte.',
				};
				modalStore.trigger(modal);
			}
			else if(r.response == true){
				console.log("Updating...")
				data.allCars = await axios.get('http://127.0.0.1:8000/autos').then((res) => res.data);
				console.log("Updated")
				const modal: ModalSettings = {
					type: 'alert',
					// Data
					title: 'Registro exitoso.',
					body: 'Se ha logrado registrar el vehículo con éxito.',
				};
				modalStore.trigger(modal);
			}
			//Trigger modal de exito.
			console.log('resolved response', r);
		});
	}

	// const tableSimple : TableSource = {
	// 	head: ['ID', 'Name'],
	// 	// body: tableMapperValues(paginatedSource, ['url', 'name']),
	// }

	let is_selected = false;

	let table_item1: HTMLElement | null = null;
</script>

<!-- <Table source={tableSimple} interactive={true} /> -->
<svelte:head>
	<title>Patentes</title>
</svelte:head>

<AppBar slotTrail="place-content-end">
	<svelte:fragment slot="lead">
		<a href="/historial">
			<picture>
				<img src={backArrow} alt="Volver" width="20" height="20" />
			</picture>
		</a>
	</svelte:fragment>
	<svelte:fragment slot="headline">
		<h1 class="h1">Patentes del Vecindario</h1>
	</svelte:fragment>

	<svelte:fragment slot="trail">
		<button type="button" class="btn-icon variant-filled-primary" on:click={logout}>
			<picture>
				<img src={logoutIcon} alt="salir" width="20" height="20" />
			</picture>
		</button>
	</svelte:fragment>
</AppBar>
<section>
	<div class="p-20">
		<Table
			source={{
				head: ['PATENTE', 'MODELO', 'AÑO'],
				body: tableMapperValues(paginatedSource, ['patente', 'modelo', 'año'])
			}}
			interactive={true}
		/>
		<!-- <Paginator bind:settings={paginationSettings} showFirstLastButtons={true} showPreviousNextButtons={true}/> -->
		<Paginator
			bind:settings={paginationSettings}
			showNumerals={true}
			justify="justify-between"
			class="mt-10"
		/>
	</div>
	<div class="flex justify-end px-20">
		<button
			type="button"
			on:click={triggerModal}
			class="btn-icon variant-filled-primary justify-self-end"
		>
			<picture>
				<img src={plusIcon} alt="salir" width="20" height="20" />
			</picture>
		</button>
	</div>
</section>

<Modal components={modalRegistry} />
