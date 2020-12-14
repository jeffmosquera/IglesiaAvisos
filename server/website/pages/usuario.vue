<template>
  <section class="container section">
    <div class="columns ">
      <div class="column is-12 box">
        <p v-if="editarUsuario" class="is-size-4 has-text-weight-bold">
          Editando usuario
        </p>
        <p v-if="!editarUsuario" class="is-size-4 has-text-weight-bold">
          Creando usuario
        </p>
        <ValidationObserver ref="observer" v-slot="{}">
          <form @submit.prevent="submit()">
            <ValidationProvider
              v-slot="{ errors }"
              name="correo"
              rules="required"
            >
              <b-field
                label="Nombre"
                :type="{ 'is-danger': errors != undefined ? false : true }"
                :message="errors"
              >
                <b-input
                  v-model="nombre"
                  placeholder="Nombre"
                  type="text"
                  :icon-right="nombre.length > 0 ? 'close-circle' : ''"
                  icon-right-clickable
                  @icon-right-click="nombre = ''"
                ></b-input>
              </b-field>
            </ValidationProvider>
            <ValidationProvider
              v-slot="{ errors }"
              name="correo"
              rules="required|email"
            >
              <b-field
                label="Correo"
                :type="{ 'is-danger': errors != undefined ? false : true }"
                :message="errors"
              >
                <b-input
                  v-model="correo"
                  placeholder="Correo"
                  type="email"
                  :icon-right="correo.length > 0 ? 'close-circle' : ''"
                  icon-right-clickable
                  @icon-right-click="correo = ''"
                ></b-input>
              </b-field>
            </ValidationProvider>

            <div class="buttons">
              <b-button
                type="submit is-primary submit"
                expanded
                @click="submit()"
              >
                Guardar
              </b-button>
            </div>
          </form>
          <b-loading
            :is-full-page="true"
            :active.sync="cargando"
            :can-cancel="false"
          ></b-loading>
        </ValidationObserver>
      </div>
    </div>
  </section>
</template>

<script>
import { mapState, mapActions, mapMutations } from 'vuex'
import { required, email, max } from 'vee-validate/dist/rules'
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode
} from 'vee-validate'
setInteractionMode('eager')
extend('required', {
  ...required,
  message: 'El campo de {_field_} no puede estar vacío'
})
extend('max', {
  ...max,
  message: 'El campo {_field_} no puede ser mayor a {length} caracteres'
})
extend('email', {
  ...email,
  message: 'Correo no es válido'
})

export default {
  layout: 'default',
  components: {
    ValidationProvider,
    ValidationObserver
  },
  data: () => ({
    nombre: '',
    correo: '',
    cargando: false
  }),
  computed: {
    ...mapState({
      usuario: (state) => state.iglesia.usuario,
      editarUsuario: (state) => state.iglesia.editarUsuario,
      sessionFlag: (state) => state.iglesia.sessionFlag
    })
  },
  created() {
    if (this.editarUsuario) {
      this.nombre = this.usuario.nombre
      this.correo = this.usuario.correo
    } else {
      this.nombre = ''
      this.correo = ''
    }
  },
  mounted() {
    if (!this.sessionFlag) {
      this.$router.push('/')
    }
  },
  methods: {
    ...mapActions({
      crearUsuario: 'iglesia/crearUsuario',
      editarUsuarioAction: 'iglesia/editarUsuarioAction',
      conseguirUsuarios: 'iglesia/conseguirUsuarios',
      borrarUsuario: 'iglesia/borrarUsuario'
    }),
    ...mapMutations({
      guardarUsuario: 'iglesia/guardarUsuario'
    }),
    submit() {
      this.cargando = true
      this.$refs.observer.validate().then((result) => {
        if (result) {
          this.onGuardarUsuario()
        } else {
          this.cargando = false
        }
      })
    },
    async onGuardarUsuario() {
      if (this.nombre === '' || this.correo === '') {
        this.$buefy.toast.open({
          duration: 5000,
          message: 'Datos incorrectos',
          position: 'is-bottom',
          type: 'is-danger'
        })
        this.cargando = false
        return
      }
      if (this.editarUsuario) {
        await this.editarUsuarioAction({
          _id: this.usuario._id,
          nombre: this.nombre,
          correo: this.correo,
          edad: this.edad
        })
      } else {
        await this.crearUsuario({
          nombre: this.nombre,
          correo: this.correo,
          edad: this.edad
        })
          .then(async (result) => {
            this.$buefy.toast.open({
              duration: 5000,
              message: result.message,
              position: 'is-bottom',
              type: 'is-danger'
            })
            await this.conseguirUsuarios()

            this.cargando = false
            this.$router.push('/usuarios')
          })
          .catch((error) => {
            this.$buefy.toast.open({
              duration: 5000,
              message: error.message,
              position: 'is-bottom',
              type: 'is-danger'
            })
            this.cargando = false
            return true
          })
      }
    },
    async onBorrarUsuario(usuario) {
      await this.borrarUsuario(usuario)
      await this.conseguirUsuarios()
    }
  }
}
</script>
