<script lang="ts">
  	import tableTest from './tableTest.svelte';

	import type { PageData } from './$types';
	import { Table, tableMapperValues } from '@skeletonlabs/skeleton';
	import type { PaginationSettings, TableSource } from '@skeletonlabs/skeleton';
	import { Paginator } from '@skeletonlabs/skeleton';

	export let data: PageData;

	let paginationSettings = {
		page: 0,
		limit: 5,
		size: data.allpokemon.results.length,
		amounts: [1,2,5,10],
	} satisfies PaginationSettings;

	$: paginatedSource = data.allpokemon.results.slice(
		paginationSettings.page * paginationSettings.limit,
		paginationSettings.page * paginationSettings.limit + paginationSettings.limit
	);

	// const tableSimple : TableSource = {
	// 	head: ['ID', 'Name'],
	// 	// body: tableMapperValues(paginatedSource, ['url', 'name']),
	// }


    let is_selected = false;

    let table_item1 : HTMLElement | null = null;

    $: {
        if(table_item1 != null){
            
        }
    }

</script>

<!-- <Table source={tableSimple} interactive={true} /> -->
<section>
	<Table source={{head: ['URL', 'NAME'], body: tableMapperValues(paginatedSource, ['url','name'])}} interactive={true}/>
	<!-- <Paginator bind:settings={paginationSettings} showFirstLastButtons={true} showPreviousNextButtons={true}/> -->
	<Paginator bind:settings={paginationSettings} showNumerals="{true}" justify="justify-between" />
</section>

