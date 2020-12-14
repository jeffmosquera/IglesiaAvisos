<template>
  <section class="container section">
    <div v-if="tablas" class="columns ">
      <div class="column is-12 box">
        <div>
          <b-table
            :data="usuarios"
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

              <b-table-column field="telefono" label="Teléfono">
                {{ props.row.telefono }}
              </b-table-column>

              <b-table-column field="nombre" label="Accciones">
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
                  <p>No hay usuarios.</p>
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
            Usuario
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
                  class="margen_abajo"
                >
                  <b-input
                    v-model="telefono"
                    placeholder="Teléfono"
                    type="text"
                    size="is-large"
                  ></b-input>
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
      editarUsuarioFlag: false,
      nombre: '',
      telefono: '',
      id: '',
      cargando: false
    }
  },
  computed: {
    ...mapState({
      usuarios: (state) => state.iglesia.usuarios,
      sessionFlag: (state) => state.iglesia.sessionFlag
    })
  },
  async mounted() {
    if (!this.sessionFlag) {
      this.$router.push('/')
    }
    this.tablas = true
    await this.conseguirUsuarios()
  },
  methods: {
    ...mapActions({
      conseguirUsuarios: 'iglesia/conseguirUsuarios',
      editarUsuario: 'iglesia/editarUsuario',
      borrarUsuario: 'iglesia/borrarUsuario'
    }),
    async onBorrarUsuario(usuario) {
      await this.borrarUsuario(usuario)
      await this.conseguirUsuarios()
    },
    onEditarUsuario(usuario) {
      this.tablas = false
      this.crear = false
      this.editar = true
      this.editarUsuarioFlag = true
      this.nombre = usuario.nombre
      this.telefono = usuario.telefono
      this.id = usuario._id
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
      if (this.nombre === '' || this.telefono === '') {
        this.$buefy.toast.open({
          duration: 5000,
          message: 'Verificar que todos los campos requeridos esten llenados',
          position: 'is-bottom',
          type: 'is-danger'
        })
        this.cargando = false
      }
      await this.editarUsuario({
        _id: this.id,
        nombre: this.nombre,
        telefono: this.telefono
      })
        .then(async (result) => {
          this.$buefy.toast.open({
            duration: 5000,
            message: result.message,
            position: 'is-bottom',
            type: 'is-success'
          })
          await this.conseguirUsuarios()

          this.cargando = false
          this.editar = false
          this.editarUsuarioFlag = false
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
</script>

<style scoped>
img {
  height: 60px;
}
.margen_abajo {
  margin-bottom: 25px;
}
</style>
