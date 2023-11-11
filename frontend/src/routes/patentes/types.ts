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