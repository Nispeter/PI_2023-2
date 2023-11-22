<script lang="ts">
	import type { SvelteComponent } from 'svelte';

	// Stores
	import { getModalStore } from '@skeletonlabs/skeleton';
	// import { isAuthenticated } from '../../store';
	// import { get } from 'svelte/store';
	// import { goto } from '$app/navigation';
	// import axios, { AxiosError } from 'axios';

	type postData = {
		modelo: string;
		rut: string;
		patente: string;
		year: string;
	};
	// Props
	/** Exposes parent props to this component. */
	export let parent: SvelteComponent;

	const modalStore = getModalStore();

	// Form Data
	const formData: postData = {
		modelo: 'Subaru',
		rut: '11.111.111-1',
		patente: 'ABCD-11',
		year: '2023'
	};
	// onMount(async ()=> {
	// 	if(!get(isAuthenticated)){
	// 		console.log("a")
	// 		goto("/login")
	// 	}
	// })

	// We've created a custom submit function to pass the response and close the modal.
	function onFormSubmit() {
		if ($modalStore[0].response) {
			/**
			  esto devuelve la form data como respuesta del modal
			  Puedes hacer el post aqui mismo
			  si pones el post aqui debes esperar la respuesta 
			https://www.skeleton.dev/utilities/modals#async-response			  

			 **/

			$modalStore[0].response(formData);
		}
		// cerrar el modal
		modalStore.close();
	}
	// function FormSubmit():void{
	// 	if($modalStore[0].response){
	// 		dispatch('formData', formData);
	// 	}
	// }

	// Base Classes
	const cBase = 'card p-4 w-modal shadow-xl space-y-4';
	const cHeader = 'text-2xl font-bold';
	const cForm = 'border border-surface-500 p-4 space-y-4 rounded-container-token';
</script>

<!-- @component This example creates a simple form modal. -->

{#if $modalStore[0]}
	<div class="modal-example-form {cBase}">
		<header class={cHeader}>{$modalStore[0].title ?? '(title missing)'}</header>
		<article>{$modalStore[0].body ?? '(body missing)'}</article>
		<!-- Enable for debugging: -->
		<form class="modal-form {cForm}">
			<label class="label">
				<span>Modelo</span>
				<input
					class="input"
					type="text"
					bind:value={formData.modelo}
					name="modelo"
					placeholder="Ingresar nombre..."
				/>
			</label>
			<label class="label">
				<span>RUT</span>
				<input
					class="input"
					type="text"
					bind:value={formData.rut}
					name="rut"
					placeholder="Ingresar rut..."
				/>
			</label>
			<label class="label">
				<span>Patente</span>
				<input
					class="input"
					type="text"
					bind:value={formData.patente}
					name="patente"
					placeholder="Ingresar patente..."
				/>
			</label>
			<label class="label">
				<span>Año</span>
				<input
					class="input"
					type="text"
					bind:value={formData.year}
					name="año"
					placeholder="Ingresar año..."
				/>
			</label>
		</form>
		<!-- prettier-ignore -->
		<footer class="modal-footer {parent.regionFooter}">
        <button class="btn {parent.buttonNeutral}" on:click={parent.onClose}>{parent.buttonTextCancel}</button>
        <button class="btn {parent.buttonPositive}" on:click={onFormSubmit}>Submit Form</button>
    </footer>
	</div>
{/if}
