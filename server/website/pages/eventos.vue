<template>
  <section class="container section">
    <div v-if="tablas" class="columns ">
      <div class="column is-12 box">
        <p class="is-size-4 has-text-weight-bold margen_abajo">Eventos</p>
        <b-button
          class="button is-link"
          size="is-medium"
          @click="onAgregarEvento"
          >Agregar</b-button
        >
        <div>
          <b-table
            :data="eventos"
            :paginated="isPaginated"
            :per-page="perPage"
            :current-page.sync="currentPage"
            :pagination-simple="isPaginationSimple"
            :pagination-position="paginationPosition"
            :default-sort-direction="defaultSortDirection"
            :sort-icon="sortIcon"
            :sort-icon-size="sortIconSize"
            aria-next-label="Next page"
            aria-previous-label="Previous page"
            aria-page-label="Page"
            aria-current-label="Current page"
          >
            <template slot-scope="props">
              <b-table-column field="nombre" label="Fecha">
                {{ $moment(props.row.creado).format('DD-MM-YYYY h:mm:ss a') }}
              </b-table-column>

              <b-table-column field="nombre" label="Nombre">
                {{ props.row.nombre }}
              </b-table-column>

              <b-table-column field="descripcion" label="Descripción">
                {{ props.row.descripcion }}
              </b-table-column>

              <b-table-column field="datetimeDate" label="Fecha de evento">
                {{
                  $moment(props.row.datetimeDate).format('DD-MM-YYYY h:mm:ss a')
                }}
              </b-table-column>

              <b-table-column field="nombre" label="Accciones">
                <button
                  class="button is-info"
                  @click="onPublicarEvento(props.row)"
                >
                  Publicar
                </button>
                <button
                  class="button is-link"
                  @click="onEditarUsuario(props.row)"
                >
                  Editar
                </button>
                <button
                  class="button is-danger"
                  @click="onBorrarUsuario(props.row)"
                >
                  Borrar
                </button>
              </b-table-column>
            </template>
            <template slot="empty">
              <section class="section">
                <div class="content has-text-grey has-text-centered">
                  <p>No hay eventos.</p>
                </div>
              </section>
            </template>
          </b-table>
        </div>
      </div>
    </div>
    <div v-if="editar">
      <div class="columns is-centered">
        <div class="column is-6">
          <p class="is-size-4 has-text-weight-bold margen_abajo">
            Evento
          </p>
          <ValidationObserver ref="observer" v-slot="{}">
            <form @submit.prevent="submit()">
              <ValidationProvider
                v-slot="{ errors }"
                name="nombre"
                rules="required"
              >
                <b-field
                  :type="{ 'is-danger': errors.length > 0 ? true : false }"
                  :message="errors"
                >
                  <b-input
                    v-model="nombre"
                    placeholder="Nombre"
                    type="text"
                    size="is-large"
                  ></b-input>
                </b-field>
              </ValidationProvider>
              <ValidationProvider
                v-slot="{ errors }"
                name="correo"
                rules="required"
              >
                <b-field
                  :type="{ 'is-danger': errors.length > 0 ? true : false }"
                  :message="errors"
                >
                  <b-input
                    v-model="descripcion"
                    placeholder="Descripcion"
                    type="textarea"
                    size="is-large"
                  ></b-input>
                </b-field>
              </ValidationProvider>
              <ValidationProvider
                v-slot="{ errors }"
                name="correo"
                rules="required"
              >
                <b-field
                  class="margen_abajo"
                  :type="{ 'is-danger': errors.length > 0 ? true : false }"
                  :message="errors"
                >
                  <b-datepicker
                    v-model="fecha_evento"
                    :day-names="['D', 'L', 'M', 'M', 'J', 'V', 'S']"
                    :month-names="[
                      'Enero',
                      'Febrero',
                      'Marzo',
                      'Abril',
                      'Mayo',
                      'Junio',
                      'Julio',
                      'Agosto',
                      'Septiembre',
                      'Octubre',
                      'Noviembre',
                      'Diciembre'
                    ]"
                    placeholder="Fecha evento..."
                    size="is-large"
                  >
                  </b-datepicker>
                </b-field>
              </ValidationProvider>
              <ValidationProvider
                v-slot="{ errors }"
                name="correo"
                rules="required"
              >
                <b-field
                  class="margen_abajo"
                  :type="{ 'is-danger': errors.length > 0 ? true : false }"
                  :message="errors"
                >
                  <b-timepicker
                    v-model="hora_evento"
                    size="is-large"
                  ></b-timepicker>
                </b-field>
              </ValidationProvider>

              <div class="buttons mt-4">
                <b-button
                  type="submit is-primary submit"
                  expanded
                  size="is-large"
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
    </div>
  </section>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { required } from 'vee-validate/dist/rules'
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode
} from 'vee-validate'
setInteractionMode('eager')
extend('required', {
  ...required,
  message: 'Este campo es requerido'
})

export default {
  components: { ValidationProvider, ValidationObserver },
  layout: 'default',
  data() {
    return {
      cargando_tabla: false,
      isPaginated: true,
      isPaginationSimple: false,
      paginationPosition: 'bottom',
      defaultSortDirection: 'asc',
      sortIcon: 'arrow-up',
      sortIconSize: 'is-small',
      currentPage: 1,
      perPage: 20,
      tablas: false,
      editar: false,
      crear: false,
      editarEventoFlag: false,
      nombre: '',
      descripcion: '',
      fecha: '',
      id: '',
      cargando: false,
      fecha_evento: new Date(),
      hora_evento: new Date()
    }
  },
  computed: {
    ...mapState({
      eventos: (state) => state.iglesia.eventos,
      sessionFlag: (state) => state.iglesia.sessionFlag
    })
  },
  async mounted() {
    if (!this.sessionFlag) {
      this.$router.push('/')
    }
    this.tablas = true
    await this.conseguirEventos()
  },
  methods: {
    ...mapActions({
      conseguirEventos: 'iglesia/conseguirEventos',
      crearEvento: 'iglesia/crearEvento',
      editarEvento: 'iglesia/editarEvento',
      borrarEvento: 'iglesia/borrarEvento',
      publicarEvento: 'iglesia/publicarEvento'
    }),
    onPublicarEvento(evento) {
      this.publicarEvento(evento)
    },
    async onBorrarUsuario(usuario) {
      await this.borrarEvento(usuario)
      await this.conseguirEventos()
    },
    onAgregarEvento() {
      this.tablas = false
      this.crear = false
      this.editar = true
      this.editarEventoFlag = false
      this.nombre = ''
      this.descripcion = ''
      this.fecha = ''
      this.id = ''
      this.fecha_evento = new Date()
      this.hora_evento = new Date()
    },
    onEditarUsuario(evento) {
      this.tablas = false
      this.crear = false
      this.editar = true
      this.editarEventoFlag = true
      this.nombre = evento.nombre
      this.descripcion = evento.descripcion
      this.fecha_evento = new Date(evento.datetimeDate)
      this.hora_evento = new Date(evento.datetimeDate)
      this.id = evento._id
    },
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
      if (this.nombre === '' || this.descripcion === '') {
        this.$buefy.toast.open({
          duration: 5000,
          message: 'Verificar que todos los campos requeridos esten llenados',
          position: 'is-bottom',
          type: 'is-danger'
        })
        this.cargando = false
      }
      this.fecha_evento.setHours(this.fecha_evento.getHours() - 5)
      this.hora_evento.setHours(this.hora_evento.getHours() - 5)
      let strFechaEvento = this.fecha_evento.toISOString()
      strFechaEvento = strFechaEvento.substring(0, 10)
      let strHoraEvento = this.hora_evento.toISOString()
      strHoraEvento = strHoraEvento.substring(10)
      const strNewDate = strFechaEvento + strHoraEvento
      const timestampDate = new Date(strNewDate).getTime() / 1000

      this.fecha_evento.setHours(this.fecha_evento.getHours() + 5)
      this.hora_evento.setHours(this.hora_evento.getHours() + 5)

      if (this.editarEventoFlag === true) {
        await this.editarEvento({
          _id: this.id,
          nombre: this.nombre,
          descripcion: this.descripcion,
          timestampDate
        })
          .then(async (result) => {
            this.$buefy.toast.open({
              duration: 5000,
              message: result.message,
              position: 'is-bottom',
              type: 'is-success'
            })
            await this.conseguirEventos()

            this.cargando = false
            this.editar = false
            this.editarEventoFlag = false
            this.tablas = true
          })
          .catch((error) => {
            this.$buefy.toast.open({
              duration: 5000,
              message: error.message,
              position: 'is-bottom',
              type: 'is-danger'
            })
            this.cargando = false
          })
      } else {
        await this.crearEvento({
          nombre: this.nombre,
          descripcion: this.descripcion,
          timestampDate
        })
          .then(async (result) => {
            this.$buefy.toast.open({
              duration: 5000,
              message: result.message,
              position: 'is-bottom',
              type: 'is-success'
            })
            await this.conseguirEventos()

            this.cargando = false
            this.editar = false
            this.editarEventoFlag = false
            this.tablas = true
          })
          .catch((error) => {
            this.$buefy.toast.open({
              duration: 5000,
              message: error.message,
              position: 'is-bottom',
              type: 'is-danger'
            })
            this.cargando = false
          })
      }
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
