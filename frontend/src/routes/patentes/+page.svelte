<script lang="ts">
	import type { PageData } from './$types';

	export let data: PageData;

    let is_selected = false;

    let table_item1 : HTMLElement | null = null;

    $: {
        if(table_item1 != null){
            
        }
    }

</script>

<div class="bg-slate flex justify-center">
	<table class="table-fixed">
		<thead class="">
			<tr class="border-bottom">
                <th><input type="checkbox" class="rounded-lg w-5 h-5 accent-green-800"></th>
				<th>Song</th>
				<th>Artist</th>
				<th>Year</th>
			</tr>
		</thead>
		<tbody class="text-left">
			<tr class="border-bottom" id="row1">
                <td class="p-3"><input type="checkbox" class="rounded-lg w-5 h-5 accent-green-800"></td>
				<td class="p-3 text-sm text-green">The Sliding Mr. Bones (Next Stop, Pottersville)</td>
                <td class="p-3 text-sm text-green">Malcolm Lockyer</td>
				<td class="p-3 text-sm text-green">1961</td>
			</tr>
			<tr class="border-bottom">
                <td class="p-3"><input type="checkbox" class="rounded-lg w-5 h-5 accent-green-800"></td>
				<td class="p-3 text-sm text-green">Witchy Woman</td>
				<td class="p-3 text-sm text-green">The Eagles</td>
				<td class="p-3 text-sm text-green">1972</td>
			</tr>
			<tr class="border-bottom">
                <td class="p-3"><input type="checkbox" class="rounded-lg w-5 h-5 accent-green-800"></td>
				<td class="p-3 text-sm text-green">Shining Star</td>
				<td class="p-3 text-sm text-green">Earth, Wind, and Fire</td>
				<td class="p-3 text-sm text-green">1975</td>
			</tr>
		</tbody>
	</table>
</div>

<style>
	.border-bottom {
        border-bottom: 1px solid gray;
	}
</style>
