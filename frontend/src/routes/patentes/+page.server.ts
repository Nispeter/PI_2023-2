import type { Car, ManyPokemon } from './types';
import axios from 'axios';

export const load = (async () => {
	const allpokemon: ManyPokemon = await axios('https://pokeapi.co/api/v2/pokemon').then(
		(res) => res.data
	);
	const allCars: Car[] = await axios('http://127.0.0.1:8000/autos').then(
		(res) => res.data
	)
	return {
		allpokemon, allCars
	};
});

export const actions = {
	default: async({request}) => {
		console.log(request.formData());
	}
};