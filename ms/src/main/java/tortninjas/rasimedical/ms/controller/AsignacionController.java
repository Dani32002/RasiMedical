package tortninjas.rasimedical.ms.controller;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.ProtocolException;
import java.net.URL;
import java.util.List;
import java.util.Optional;

import org.json.JSONArray;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import tortninjas.rasimedical.ms.model.Asignacion;
import tortninjas.rasimedical.ms.model.AsignacionRepository;

@RestController
public class AsignacionController {

    private AsignacionRepository asignacionRepository;

    @Autowired
    public AsignacionController(AsignacionRepository asignacionRepository) {
        this.asignacionRepository = asignacionRepository;
    }

    @PostMapping
    @ResponseStatus(code = HttpStatus.CREATED)
    public Asignacion addAsignacion(@RequestBody Asignacion asignacion){
        return asignacionRepository.save(asignacion);
    }

    @GetMapping()
    @ResponseStatus(code = HttpStatus.OK)
    public List<Asignacion> getAll() {
        return asignacionRepository.findAll();
    } 

    @GetMapping(value = "/medico/{id}")
    @ResponseStatus(code = HttpStatus.OK)
    public List<Asignacion> getAllMedico(@PathVariable Long id) {
        return asignacionRepository.findByMedico(id);
    } 

    @GetMapping(value = "/tipo/{tipo}")
    @ResponseStatus(code = HttpStatus.OK)
    public List<Asignacion> getAllTipo(@PathVariable String tipo) {
        return asignacionRepository.findByTipo(tipo);
    } 

    @GetMapping(value = "/tipo/{tipo}/elemento/{id}")
    @ResponseStatus(code = HttpStatus.OK)
    public List<Asignacion> getAllTipoElemento(@PathVariable String tipo, @PathVariable Long id) {
        return asignacionRepository.findByTipoAndElemento(tipo, id);
    } 

    @GetMapping(value = "/activo/{activo}")
    @ResponseStatus(code = HttpStatus.OK)
    public List<Asignacion> getAllActivo(@PathVariable Boolean activo) {
        return asignacionRepository.findByActivo(activo);
    } 
    
    @GetMapping(value = "/{id}")
    @ResponseStatus(code = HttpStatus.OK)
    public Asignacion findOne(@PathVariable("id") Long id) throws Exception {
        Optional<Asignacion> asignacion = asignacionRepository.findById(id);
        if (asignacion.isEmpty())
            throw new Exception("Entity doesn't exist");
        return asignacion.get();
    }

    @DeleteMapping(value = "/{id}")
    @ResponseStatus(code = HttpStatus.NO_CONTENT)
    public void delete(@PathVariable Long id) throws Exception {
        Optional<Asignacion> asignacion = asignacionRepository.findById(id);
        if (asignacion.isEmpty())
            throw new Exception("Entity doesn't exist");
        asignacionRepository.deleteById(asignacion.get().getId());
    }

    @PutMapping(value = "/{id}")
    @ResponseStatus(code = HttpStatus.OK)
    public Asignacion update(@PathVariable Long id, @RequestBody Asignacion asignacion) throws Exception {
        Optional<Asignacion> asignacionOG = asignacionRepository.findById(id);
        if (asignacionOG.isEmpty())
            throw new Exception("Entity doesn't exist");
        asignacion.setId(asignacionOG.get().getId());
        return asignacionRepository.save(asignacion);
    }


    public Boolean CheckElemento(Asignacion asignacion) throws IOException {
        JSONObject json = peticion("Elemento");
        JSONArray arr = json.getJSONArray("");
        for (int i = 0; i < arr.length(); i++) {
            if (Long.parseLong(arr.getJSONObject(i).getString("id")) == asignacion.getElemento()) {
                return true;
            }
        }
        return false;
    }

    public JSONObject peticion(String forma) throws IOException {
        URL url = new URL("http://example.com");
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("Content-Type", "application/json");
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer content = new StringBuffer();
        while ((inputLine = in.readLine()) != null) {
            content.append(inputLine);
        }
        in.close();
        con.disconnect();
        String respuesta = content.toString();
        JSONObject json = new JSONObject(respuesta); 
        return json;
    }
}
