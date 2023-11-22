export interface Lugar{
    cam_id: string
}

export interface Propietario{
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
    año: 1964,
    propietario: Propietario
}