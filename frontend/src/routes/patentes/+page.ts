import type { Car, ManyPokemon } from './types';
import axios from 'axios';

export const load = (async () => {
	const allCars: Car[] = await axios('http://127.0.0.1:8000/autos').then(
		(res) => res.data
	)
	return {
		allCars
	};
});
