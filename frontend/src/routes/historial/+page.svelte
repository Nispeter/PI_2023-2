<script lang="ts">
	import { Table } from '@skeletonlabs/skeleton';
	import type { TableSource } from '@skeletonlabs/skeleton';
	import { tableMapperValues } from '@skeletonlabs/skeleton';
	import { Avatar } from '@skeletonlabs/skeleton';
	import { AppShell } from '@skeletonlabs/skeleton';

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

<div class="absolute top-0 right-0">
	<button type="button" class="btn btn-xl variant-filled">Administrar Datos</button>
</div>
<h1>
	<strong> Bienvenidos a su aplicacion de reconocimiento de vehiculos </strong>
</h1>

<Table source={tableSimple} />

<div class="table-container">
	<table class="table table-hover">
		<thead>
			<tr>
				<th>Nombre</th>
				<th>Número Patente</th>
				<th>Hora</th>
				<th>Fecha</th>
			</tr>
		</thead>
		<tbody>
			{#each sourceData as row, i}
				<tr>
					<td>{row.nombreDueño}</td>
					<td>{row.nPatente}</td>
					<td>{row.Hora}</td>
					<td>{row.Fecha}</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
