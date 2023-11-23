export type Lugar = {
    cam_id: string
}

export type Propietario = {
    id: string,
    rut: string,
    nombre: string,
    rol: string
}

export interface DataH{
    id: string,
    car_id: number,
    time: string,
    lugar: Lugar
    licence: string,
    probability: number
}

export interface Dueño{
    id: string,
    patente: string,
    modelo: string,
    año: string,
    propietario: Propietario
}