<template>
  <section class="hero is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-5-tablet is-4-desktop is-4-widescreen">
            <p class="is-size-3 has-text-weight-bold has-text-centered">
              <img src="~/assets/logo.png" />
            </p>
            <ValidationObserver ref="observer" v-slot="{}">
              <form class="" @submit.prevent="submit()">
                <ValidationProvider
                  v-slot="{ errors }"
                  name="correo"
                  rules="required|email"
                >
                  <b-field
                    :type="{ 'is-danger': errors != undefined ? false : true }"
                    :message="errors"
                    class="mb-6"
                  >
                    <b-input
                      v-model="correo"
                      placeholder="Correo"
                      type="email"
                      size="is-large"
                      :icon-right="correo.length > 0 ? 'close-circle' : ''"
                      icon-right-clickable
                      @icon-right-click="correo = ''"
                    ></b-input>
                  </b-field>
                </ValidationProvider>
                <ValidationProvider
                  v-slot="{ errors }"
                  name="clave"
                  rules="required"
                >
                  <b-field :type="{ 'is-danger': false }" :message="errors">
                    <b-input
                      v-model="clave"
                      placeholder="Clave"
                      type="password"
                      size="is-large"
                      :icon-right="clave.length > 0 ? 'close-circle' : ''"
                      icon-right-clickable
                      @icon-right-click="clave = ''"
                    ></b-input>
                  </b-field>
                </ValidationProvider>
                <div class="buttons">
                  <b-button
                    type="submit is-black"
                    size="is-large"
                    expanded
                    @click="submit()"
                    >Entrar</b-button
                  >
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
      </div>
    </div>
  </section>
</template>

<script>
// import axios from 'axios'
import { mapActions } from 'vuex'
import { required, email } from 'vee-validate/dist/rules'
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode
} from 'vee-validate'
setInteractionMode('eager')
extend('required', {
  ...required,
  message: 'Este campo es requerido.'
})
extend('email', {
  ...email,
  message: 'El correo ingresado no esta válido.'
})
export default {
  layout: 'blank',
  components: {
    ValidationProvider,
    ValidationObserver
  },
  data: () => ({
    correo: '',
    clave: '',
    cargando: false
  }),
  created() {
    if (this.sessionFlag) {
      this.$router.push('/eventos')
    } else {
      this.$router.push('/')
    }
  },
  methods: {
    ...mapActions({
      loginAdministrador: 'iglesia/loginAdministrador'
    }),
    submit() {
      this.cargando = true
      this.$refs.observer.validate().then((result) => {
        if (result) {
          this.onLogin()
        } else {
          this.cargando = false
        }
      })
    },
    onLogin() {
      this.loginAdministrador({ correo: this.correo, clave: this.clave })
        .then(() => {
          this.$router.push('/eventos')
        })
        .catch((error) => {
          this.cargando = false
          this.$buefy.toast.open({
            duration: 5000,
            message: error.message,
            position: 'is-bottom',
            type: 'is-danger'
          })
        })
    }
  }
}
</script>
