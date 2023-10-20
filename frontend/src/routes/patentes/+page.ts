import type { PageLoad } from './$types';
import type { ManyPokemon, Pokemon } from './types';

export const load = (async () => {
    const allpokemon:ManyPokemon = await fetch('https://pokeapi.co/api/v2/pokemon').then(res => res.json());
    return {
        allpokemon
    };
}) satisfies PageLoad;