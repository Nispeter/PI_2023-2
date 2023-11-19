<script lang="ts">
	import  type { SvelteComponent }  from 'svelte';

	// Stores
	import { getModalStore } from '@skeletonlabs/skeleton';
	import { isAuthenticated } from '../../store';
	import { get } from 'svelte/store';
	import { goto } from '$app/navigation';
	import axios, {AxiosError} from 'axios';

	// Props
	/** Exposes parent props to this component. */
	export let parent: SvelteComponent;

	const modalStore = getModalStore();

	// Form Data
	const formData = {
		name: 'Jane Doe',
		rut: '11.111.111-1',
		patente: 'ABCD-11',
		año: '2023',
		propietario: [
			"653cd32c3b930cb8658f685b"
		]
	};
	// onMount(async ()=> {
	// 	if(!get(isAuthenticated)){
	// 		console.log("a")
	// 		goto("/login")
	// 	}
	// })

	// We've created a custom submit function to pass the response and close the modal.
	async function onFormSubmit(): Promise<void> {

		if ($modalStore[0].response){
			$modalStore[0].response(formData);
		}

		try{
			const response = await axios.post('http://127.0.0.1:8000/autos', formData);
			console.log(response.data);
		}catch(e){
			if(axios.isAxiosError(e)){
				console.log(e.response);
			}
		} 
		
		console.log(formData);
		modalStore.close();
	}

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
		<form class="modal-form {cForm}" method="POST">
			<label class="label">
				<span>Name</span>
				<input class="input" type="text" bind:value={formData.name} name="name" placeholder="Ingresar nombre..." />
			</label>
			<label class="label">
				<span>RUT</span>
				<input class="input" type="text" bind:value={formData.rut} name="rut" placeholder="Ingresar rut..." />
			</label>
			<label class="label">
				<span>Email</span>
				<input class="input" type="text" bind:value={formData.patente} name="patente" placeholder="Ingresar patente..." />
			</label>
		</form>
		<!-- prettier-ignore -->
		<footer class="modal-footer {parent.regionFooter}">
        <button class="btn {parent.buttonNeutral}" on:click={parent.onClose}>{parent.buttonTextCancel}</button>
        <button class="btn {parent.buttonPositive}" on:click={onFormSubmit}>Submit Form</button>
    </footer>
	</div>
{/if}