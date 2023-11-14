<script lang="ts">
	import { auth } from '$lib/auth';
	import type { PageData } from './$types';
	import { Table, tableMapperValues } from '@skeletonlabs/skeleton';
	import type { PaginationSettings, TableSource } from '@skeletonlabs/skeleton';
	import { Paginator, AppBar } from '@skeletonlabs/skeleton';
	import { onMount } from 'svelte';
	import { isAuthenticated } from '../../store';
	import { goto } from '$app/navigation';
	import { get } from 'svelte/store';
	import backArrow from '$lib/images/back-arrow.svg'
	import logoutIcon from '$lib/images/logout.svg'
	import plusIcon from '$lib/images/plus.svg'
	import { Modal, getModalStore } from '@skeletonlabs/skeleton';
	import type { ModalSettings, ModalComponent, ModalStore } from '@skeletonlabs/skeleton';
	import modalForm from './components/modalForm.svelte'


	export let data: PageData;
			
	const modalStore = getModalStore();


	const modalComponent: ModalComponent = { ref: modalForm };

	const modal: ModalSettings = {
		title: 'Ingresar registro.',
		body: 'Rellene el formulario.',
		type: 'component',
		component: modalComponent,
	};
	// modalStore.trigger(modal);
	if ($modalStore[0]) console.log($modalStore[0].title);

	// onMount(async ()=> {
	// 	await auth.createClient();
	// 	if(!get(isAuthenticated)){
	// 		goto("/login")
	// 	}
	// })

	async function logout() {
		await auth.logout();
	}

	let paginationSettings = {
		page: 0,
		limit: 5,
		size: data.allpokemon.results.length,
		amounts: [1, 2, 5, 10]
	} satisfies PaginationSettings;

	$: paginatedSource = data.allpokemon.results.slice(
		paginationSettings.page * paginationSettings.limit,
		paginationSettings.page * paginationSettings.limit + paginationSettings.limit
	);
	let modalFlag : boolean = false;
	function triggerModal(){
		modalFlag = true;
		modalStore.trigger(modal)
	}

	// const tableSimple : TableSource = {
	// 	head: ['ID', 'Name'],
	// 	// body: tableMapperValues(paginatedSource, ['url', 'name']),
	// }

	let is_selected = false;

	let table_item1: HTMLElement | null = null;

	$: {
		if (table_item1 != null) {
		}
	}
</script>

<!-- <Table source={tableSimple} interactive={true} /> -->
<svelte:head>
	<title>Patentes</title>
</svelte:head>

<AppBar slotTrail="place-content-end">
	<svelte:fragment slot="lead">
		<a href="/historial">
			<picture>
				<img src="{backArrow}" alt="Volver" width="20" height="20">
			</picture>
		</a>
	</svelte:fragment>
	<svelte:fragment slot="headline">
		<h1 class="h1">Patentes del Vecindario</h1>
	</svelte:fragment>

	<svelte:fragment slot="trail">
		<button type="button" class="btn-icon variant-filled-primary" on:click={logout}>
			<picture>
				<img src="{logoutIcon}" alt="salir" width="20" height="20">
			</picture>
		</button>
	</svelte:fragment>
</AppBar>
<section>
	<div class="p-20">
		<Table
			source={{ head: ['URL', 'NAME'], body: tableMapperValues(paginatedSource, ['url', 'name']) }}
			interactive={true}
		/>
		<!-- <Paginator bind:settings={paginationSettings} showFirstLastButtons={true} showPreviousNextButtons={true}/> -->
		<Paginator bind:settings={paginationSettings} showNumerals={true} justify="justify-between" class='mt-10'/>
	</div>
<div class="flex justify-end px-20">
	<button type="button" on:click={triggerModal} class="btn-icon variant-filled-primary justify-self-end" on:click={logout}>
		<picture>
			<img src="{plusIcon}" alt="salir" width="20" height="20">
		</picture>
	</button>
</div>
</section>
{#if modalFlag}
	<Modal/>
{/if}