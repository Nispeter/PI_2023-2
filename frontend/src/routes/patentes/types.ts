export interface Pokemon{
    name: String
    id: number
    sprites: any

}

export interface ManyPokemon{
    count: number
    next: string
    previous: string
    results: Pokemon[]
}

export interface Car{
    id: number,
    patent: string,
    model: string,
    year: number,
    
}