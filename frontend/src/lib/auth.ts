import { createAuth0Client } from "@auth0/auth0-spa-js";
import { ENV } from "./env";

async function login(){
    const client = await createAuth0Client({
        domain: ENV.auth0.domain,
        clientId: ENV.auth0.id,
        authorizationParams: {
            redirect_uri: window.location.href
        }
    })

    client.loginWithRedirect();
}

async function logout(){

    const client = await createAuth0Client({
        domain: ENV.auth0.domain,
        clientId: ENV.auth0.id,
        authorizationParams: {
            redirect_uri: window.location.href
        }
    })

    client.logout();
}

export const auth = {
    login,
    logout
}