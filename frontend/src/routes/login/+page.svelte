<script>
	import { auth } from '$lib/auth';
</script>

<section>
	<div class="flex h-screen items-center">
		<div class="card w-1/2 mx-auto h-1/2">
			<header class="card-header text-center text-4xl">Inicio de Sesion</header>
			<div class="grid grid-cols-1 justify-items-center h-full place-content-center">
				<button class="btn rounded-md variant-filled-primary" on:click={auth.login}>Iniciar Sesion</button>
				<button class="btn rounded-md variant-filled-primary" on:click={auth.logout}>Logout</button>
			</div>
		</div>
	</div>
</section>
