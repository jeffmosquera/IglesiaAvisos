import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios'

Vue.use(Vuex)

export const state = () => {
  return {
    sessionFlag: false,
    administrador: {},
    usuarios: [],
    usuario: {},
    marcaciones: [],
    editarUsuario: false,
    fotoSeleccionada: 0,
    eventos: [],
    eventosOrdenados: [],
    pantalla: {}
  }
}

export const mutations = {
  iniciarSesion(state) {
    state.sessionFlag = true
  },
  cerrarSesion(state) {
    state.sessionFlag = false
    state.administrador = {}
  },
  guardarAdministrador(state, payload) {
    state.administrador = payload
  },
  guardarUsuarios(state, payload) {
    state.usuarios = payload
  },
  guardarUsuario(state, payload) {
    state.usuario = payload
  },
  guardarEventos(state, payload) {
    state.eventos = payload
  },
  guardarEventosOrdenados(state, payload) {
    state.eventosOrdenados = payload
  },
  guardarPantalla(state, payload) {
    state.pantalla = payload
  }
}

export const actions = {
  loginAdministrador(context, payload) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'POST',
        url: process.env.baseUrl + '/administradores/login',
        headers: { 'Content-Type': 'application/json' },
        data: { correo: payload.correo, clave: payload.clave }
      }).then(
        (result) => {
          context.commit('iniciarSesion')
          context.commit('guardarAdministrador', result.data)
          resolve(result)
        },
        (error) => {
          reject(error.response.data)
        }
      )
    })
  },
  crearEvento(context, payload) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'POST',
        url: process.env.baseUrl + '/eventos',
        headers: { 'Content-Type': 'application/json' },
        data: {
          nombre: payload.nombre,
          descripcion: payload.descripcion,
          timestampDate: payload.timestampDate
        }
      }).then(
        (result) => {
          resolve(result.data)
        },
        (error) => {
          reject(error.response.data)
        }
      )
    })
  },
  subirFotoUsuario(context, payload) {
    return new Promise((resolve, reject) => {
      const formData = new FormData()
      formData.append('file', payload.foto)
      axios({
        method: 'POST',
        url:
          process.env.baseUrl +
          '/usuarios/' +
          payload._id +
          '?foto_seleccionada=' +
          context.state.fotoSeleccionada,
        headers: { 'Content-Type': 'multipart/form-data' },
        data: formData
      }).then(
        (result) => {
          resolve(result)
        },
        (error) => {
          reject(error.response.data)
        }
      )
    })
  },
  editarUsuario(context, payload) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'PUT',
        url: process.env.baseUrl + '/usuarios/' + payload._id,
        headers: { 'Content-Type': 'application/json' },
        data: {
          nombre: payload.nombre,
          telefono: payload.telefono
        }
      }).then(
        (result) => {
          resolve(result.data)
        },
        (error) => {
          reject(error.response.data)
        }
      )
    })
  },
  editarPantalla(context, payload) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'GET',
        url:
          process.env.baseUrl +
          '/pantalla/5fc714a9828833e8d6c21719/' +
          payload.index_evento,
        headers: { 'Content-Type': 'application/json' }
      }).then(
        (result) => {
          resolve(result.data)
        },
        (error) => {
          reject(error.response.data)
        }
      )
    })
  },
  editarEvento(context, payload) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'PUT',
        url: process.env.baseUrl + '/eventos/' + payload._id,
        headers: { 'Content-Type': 'application/json' },
        data: {
          nombre: payload.nombre,
          descripcion: payload.descripcion,
          timestampDate: payload.timestampDate
        }
      }).then(
        (result) => {
          resolve(result.data)
        },
        (error) => {
          reject(error.response.data)
        }
      )
    })
  },
  publicarEvento(context, payload) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'PUT',
        url: process.env.baseUrl + '/eventos/' + payload._id + '/publicar',
        headers: { 'Content-Type': 'application/json' }
      }).then(
        (result) => {
          resolve(result.data)
        },
        (error) => {
          reject(error.response.data)
        }
      )
    })
  },
  noPublicarEvento(context, payload) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'PUT',
        url: process.env.baseUrl + '/eventos/' + payload._id + '/nopublicar',
        headers: { 'Content-Type': 'application/json' }
      }).then(
        (result) => {
          resolve(result.data)
        },
        (error) => {
          reject(error.response.data)
        }
      )
    })
  },
  async conseguirUsuarios(context) {
    await axios({
      method: 'GET',
      url: process.env.baseUrl + '/usuarios',
      headers: {
        'Content-Type': 'application/json'
      }
    }).then((result) => {
      context.commit('guardarUsuarios', result.data.usuarios)
    })
  },
  borrarUsuario(context, payload) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'DELETE',
        url: process.env.baseUrl + '/usuarios/' + payload._id,
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(
        (result) => {
          resolve(result)
        },
        (error) => {
          reject(error.response.data)
        }
      )
    })
  },
  borrarEvento(context, payload) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'DELETE',
        url: process.env.baseUrl + '/eventos/' + payload._id,
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(
        (result) => {
          resolve(result)
        },
        (error) => {
          reject(error.response.data)
        }
      )
    })
  },
  async conseguirEventos(context) {
    await axios({
      method: 'GET',
      url: process.env.baseUrl + '/eventos',
      headers: {
        'Content-Type': 'application/json'
      }
    }).then((result) => {
      context.commit('guardarEventos', result.data.eventos)
    })
  },
  async conseguirEventosOrdenados(context) {
    await axios({
      method: 'GET',
      url: process.env.baseUrl + '/eventos/ordenados',
      headers: {
        'Content-Type': 'application/json'
      }
    }).then((result) => {
      context.commit('guardarEventosOrdenados', result.data.eventos)
    })
  },
  async conseguirPantalla(context) {
    await axios({
      method: 'GET',
      url: process.env.baseUrl + '/pantalla/5fc714a9828833e8d6c21719',
      headers: {
        'Content-Type': 'application/json'
      }
    }).then((result) => {
      context.commit('guardarPantalla', result.data.pantalla)
    })
  }
}
