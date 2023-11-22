import type { DataH, Dueño, Propietario, Lugar } from './types';
import axios from 'axios';

export const load = (async () => {
	const hi: DataH[] = await axios('http://127.0.0.1:8000/horarios').then(
		(res) => res.data
	)
	return {
		hi
	};
});