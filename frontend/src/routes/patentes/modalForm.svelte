<script lang="ts">
	import { createForm } from 'svelte-forms-lib';
	import { onMount, type SvelteComponent } from 'svelte';
	import { validateRut } from '@fdograph/rut-utilities';

	// Stores
	import { getModalStore } from '@skeletonlabs/skeleton';
	import { isAuthenticated } from '../../store';
	import { get } from 'svelte/store';
	import { goto } from '$app/navigation';
	import axios from 'axios';

	/*Utilizando createForm de svelte-forms-lib podemos crear una form con distintos
	handlers, en este caso utilizamos form, que representa los datos de la form,
	errors que representa los errores en la validacion, handleChange que
	permite manejar la validacion mientras vaya cambiando el input, handleSubmit
	que maneja el submit de la form.*/
	const { form, errors, state, handleChange, handleSubmit } = createForm({
		/*Indica los valores iniciales de los campos de la form*/
		initialValues: {
			modelo: '',
			rut: '',
			patente: '',
			ano: ''
		},
		/** En esta seccion es donde se validan los valores del*/
		validate: (values: any) => {
			let errs: {
				modelo: string | null;
				rut: string | null;
				ano: string | null;
				patente: string | null;
			} = { modelo: '', rut: '', ano: '', patente: '' };
			if (values.modelo === '') {
				errs['modelo'] = 'El modelo es obligatorio.';
			}
			if (validateRut(values.rut) == false) {
				errs['rut'] = 'Rut invalido.';
			}
			if (values.año != undefined) {
				if (values.año.length > 4 || values.año.length < 4) {
					errs['ano'] = 'Año invalido.';
				}
			}
			if (values.patente != undefined) {
				if (values.patente.length < 7 || values.patente.length > 7) {
					errs['patente'] = 'Patente invalida';
				}
			}
			return errs;
		},
		onSubmit: (values: any) => {
			console.log(values);
			onFormSubmit(values);
		}
	});

	type postData = {
		modelo: string;
		rut: string;
		patente: string;
		año: string;
	};
	// Props
	/** Exposes parent props to this component. */
	export let parent: SvelteComponent;

	const modalStore = getModalStore();

	onMount(async () => {
		if (!get(isAuthenticated)) {
			goto('/login');
		}
	});

	// We've created a custom submit function to pass the response and close the modal.
	//Para validacion esta funcion va dentro del onSubmit.
	async function onFormSubmit(values: postData) {
		//console.log(validateRut(formData.rut));
		if ($modalStore[0].response) {
			/**
			  esto devuelve la form data como respuesta del modal
			  Puedes hacer el post aqui mismo
			  si pones el post aqui debes esperar la respuesta 
			https://www.skeleton.dev/utilities/modals#async-response			  

			 **/
			try {
				const response = await axios.post('http://127.0.0.1:8000/autos', values);
				$modalStore[0].response({ response: true });
				console.log('a');
			} catch (e) {
				if (axios.isAxiosError(e)) {
					console.log(e.response);
					$modalStore[0].response({ response: false });
				}
			}
		}
		// cerrar el modal
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
		<form class="modal-form {cForm}">
			<label class="label">
				<span>Modelo</span>
				<input
					class="input"
					type="text"
					on:change={handleChange}
					bind:value={$form.modelo}
					name="modelo"
					placeholder="Ingresar modelo..."
				/>
				{#if $errors.modelo}
					<small>{$errors.modelo}</small>
				{/if}
			</label>
			<label class="label">
				<span>RUT</span>
				<input
					class="input"
					type="text"
					on:change={handleChange}
					bind:value={$form.rut}
					name="rut"
					placeholder="Ingresar rut..."
				/>
				{#if $errors.rut}
					<small class="text-red-500 italic">{$errors.rut}</small>
				{/if}
			</label>
			<label class="label">
				<span>Patente</span>
				<input
					class="input"
					type="text"
					on:change={handleChange}
					bind:value={$form.patente}
					name="patente"
					placeholder="Ingresar patente..."
				/>
				{#if $errors.patente}
					<small>{$errors.patente}</small>
				{/if}
			</label>
			<label class="label">
				<span>Año</span>
				<input
					class="input"
					type="text"
					on:change={handleChange}
					bind:value={$form.ano}
					name="año"
					placeholder="Ingresar año..."
				/>
				{#if $errors.año}
					<small>{$errors.año}</small>
				{/if}
			</label>
		</form>
		<!-- prettier-ignore -->
		<footer class="modal-footer {parent.regionFooter}">
        <button class="btn {parent.buttonNeutral}" on:click={parent.onClose}>{parent.buttonTextCancel}</button>
        <button class="btn {parent.buttonPositive}" on:click={handleSubmit}>Submit Form</button>
        <!-- <button class="btn {parent.buttonPositive}" type="submit">Submit Form</button> -->
    </footer>
	</div>
{/if}
