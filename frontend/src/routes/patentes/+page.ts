import type { PageLoad } from './$types';
import type { ManyPokemon } from './types';
import axios from 'axios';

export const load = (async () => {
	const allpokemon: ManyPokemon = await axios('https://pokeapi.co/api/v2/pokemon').then(
		(res) => res.data
	);
	return {
		allpokemon
	};
}) satisfies PageLoad;
