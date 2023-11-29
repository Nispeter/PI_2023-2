import type { Car } from './types';
import axios from 'axios';

/**
 * Funcion que hace get de todos los autos registrados en la base de datos como parte de la comunidad.
 * @returns 
 */
export const load = (async () => {
	const allCars: Car[] = await axios('http://127.0.0.1:8000/autos').then(
		(res) => res.data
	)
	return {
		allCars
	};
});
