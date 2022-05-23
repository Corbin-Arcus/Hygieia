const ADD_PROFILE = 'profile/ADD_PROFILE'

const addProfile = (profile) => {
  return{
    type: ADD_PROFILE,
    payload: profile
  }
}

export const addAProfile = (user_id,
  profile_picture,
  name,
  phone_number,
  age,
  blood_type,
  allergies,
  medical_conditions,
  medications,
  medication_allergies,
  height,
  weight,
  hair_color,
  distinctive_features,
  shoe_size,
  clothing_size,
  address) => async (dispatch) => {
    const res = await fetch('/api/profile/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        user_id,
        profile_picture,
        name,
        phone_number,
        age,
        blood_type,
        allergies,
        medical_conditions,
        medications,
        medication_allergies,
        height,
        weight,
        hair_color,
        distinctive_features,
        shoe_size,
        clothing_size,
        address
      })
    })

    if (res.ok) {
      const data = await res.json()
      dispatch(addProfile(data))
      return data
    }
    else if (res.status < 500) {
      const data = await res.json()
      if (data.errors) return data.errors
    }
    else{
      return ['An error occurred. Please try again']
    }

}
