<template>
  <section class="container section">
    <div class="container">
      <div>
        <h1
          v-if="pantalla.mostrar_eventos"
          class="title  
                has-text-centered margen_abajo"
        >
          Eventos
        </h1>
        <h1
          v-if="pantalla.mostrar_evento"
          class="title  
                has-text-centered margen_abajo"
        >
          Evento
        </h1>
      </div>
      <div
        v-if="pantalla.mostrar_eventos"
        class="columns is-mobile is-centered"
      >
        <div class="column is-8">
          <div class="list">
            <ul>
              <div
                v-for="evento in eventosOrdenados"
                :key="evento._id"
                class="list-item"
              >
                <li>
                  <p class="title has-text-centered">
                    {{ evento.nombre }}
                  </p>
                  <p class="is-size-4 has-text-centered">
                    {{
                      $moment(evento.datetimeDate).format(
                        'DD-MM-YYYY h:mm:ss a'
                      )
                    }}
                  </p>
                </li>
              </div>
            </ul>
          </div>
        </div>
      </div>
      <div v-if="pantalla.mostrar_evento" class="columns is-mobile is-centered">
        <div class="column is-8">
          <div class="list">
            <ul>
              <div class="list-item">
                <li>
                  <p class="title has-text-centered">
                    {{ evento.nombre }}
                  </p>
                  <p class="title has-text-centered">
                    {{ evento.descripcion }}
                  </p>
                  <p class="is-size-4 has-text-centered">
                    {{
                      $moment(evento.datetimeDate).format(
                        'DD-MM-YYYY h:mm:ss a'
                      )
                    }}
                  </p>
                </li>
              </div>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  layout: 'blank',
  data: () => ({
    evento: {}
  }),
  computed: {
    ...mapState({
      eventosOrdenados: (state) => state.iglesia.eventosOrdenados,
      pantalla: (state) => state.iglesia.pantalla,
      sessionFlag: (state) => state.iglesia.sessionFlag
    })
  },
  created() {},
  mounted() {
    this.mostrar_eventos = true
    this.mostrar_evento = false
    this.conseguirEventosOrdenados()
    setInterval(() => {
      this.conseguirEventosOrdenados()
      this.verificar()
    }, 200)
  },
  methods: {
    ...mapActions({
      conseguirEventosOrdenados: 'iglesia/conseguirEventosOrdenados',
      conseguirPantalla: 'iglesia/conseguirPantalla'
    }),
    verificar() {
      this.conseguirPantalla()
      const indexEvento = parseInt(this.pantalla.index_evento) - 1

      if (indexEvento >= 0 && indexEvento < 10) {
        this.evento = this.eventosOrdenados[indexEvento]
      }
    },
    onSubirFotoUsuario() {
      if (this.file) {
        this.subirFotoUsuario({ _id: this.usuario._id, foto: this.file })
          .then(async () => {
            await this.conseguirUsuarios()
            this.$router.push('/usuarios')
          })
          .catch((error) => {
            this.$buefy.toast.open({
              duration: 5000,
              message: error.message,
              position: 'is-bottom',
              type: 'is-danger'
            })
          })
      } else {
        this.$buefy.toast.open({
          duration: 5000,
          message: 'Seleccione una imagen',
          position: 'is-bottom',
          type: 'is-danger'
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

<style scoped>
img {
  height: 60px;
}
.margen_abajo {
  margin-bottom: 25px;
}
</style>
